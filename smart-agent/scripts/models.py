#!/usr/bin/env python3
"""Offline, provider-agnostic model catalogs. No API calls, model execution or credential access."""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import sys

def registry_path():
    home=Path(os.environ.get('CODEX_HOME',Path.home()/'.codex')).expanduser()
    return home/'skill-state/smart-agent/model-registry.json'

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');tmp.replace(path)

def identifier(value,label):
    if not isinstance(value,str) or not value.strip() or any(ord(c)<32 for c in value):
        raise ValueError(label+' must be a nonempty string without control characters')
    return value

def field(obj,path):
    for part in path.split('.'):
        if not isinstance(obj,dict) or part not in obj:
            raise ValueError('Missing JSON field: '+path)
        obj=obj[part]
    return obj

def capabilities(raw,prefix=''):
    if raw is None:return {}
    if not isinstance(raw,dict):raise ValueError('capabilities must be a mapping')
    result={}
    for key,value in raw.items():
        if not isinstance(key,str) or not re.fullmatch(r'[\w.-]+',key):
            raise ValueError('Invalid capability name')
        name=prefix+key
        if isinstance(value,bool) or value is None:result[name]=value
        elif isinstance(value,dict):
            if 'supported' in value:
                supported=value['supported']
                if supported is not None and not isinstance(supported,bool):raise ValueError('Capability supported must be boolean or null')
                result[name]=supported
            result.update(capabilities({k:v for k,v in value.items() if k!='supported' and isinstance(v,dict)},name+'.'))
        else:raise ValueError('Capability values must be boolean, null or supported objects')
    return result

def normalize(raw,provider,observed_on,items_field=None,id_field=None):
    identifier(provider,'provider');date.fromisoformat(observed_on)
    if items_field:
        rows=field(raw,items_field)
    elif isinstance(raw,list):rows=raw
    elif isinstance(raw,dict):
        rows=next((raw[k] for k in ('data','models') if isinstance(raw.get(k),list)),None)
    else:rows=None
    if not isinstance(rows,list):raise ValueError('Expected a list, data/models array, or explicit --items-field')
    pending=bool(isinstance(raw,dict) and (raw.get('has_more') or raw.get('nextPageToken') or raw.get('next_page_token') or raw.get('next')))
    output=[];seen=set()
    for row in rows:
        if not isinstance(row,dict):raise ValueError('Each model must be an object')
        mid=field(row,id_field) if id_field else next((row[k] for k in ('id','slug','name','model') if isinstance(row.get(k),str) and row[k]),None)
        identifier(mid,'model ID')
        if mid in seen:raise ValueError('Duplicate model ID within this provider snapshot: '+mid)
        seen.add(mid)
        display=next((row[k] for k in ('display_name','displayName') if isinstance(row.get(k),str)),mid)
        caps=capabilities(row.get('capabilities'))
        if isinstance(row.get('thinking'),bool):caps.setdefault('thinking',row['thinking'])
        limits={}
        for canonical,names in {'input_tokens':['inputTokenLimit','max_input_tokens','context_window'],'output_tokens':['outputTokenLimit','max_tokens']}.items():
            value=next((row[k] for k in names if k in row),None)
            if isinstance(value,int) and not isinstance(value,bool) and value>0:limits[canonical]=value
        methods=row.get('supportedGenerationMethods',[])
        if not isinstance(methods,list) or not all(isinstance(x,str) for x in methods):raise ValueError('Generation methods must be a string array')
        efforts=row.get('supported_reasoning_levels',[])
        if not isinstance(efforts,list):raise ValueError('Reasoning levels must be an array')
        efforts=[e.get('effort') if isinstance(e,dict) else e for e in efforts]
        if not all(isinstance(e,str) for e in efforts):raise ValueError('Reasoning levels must contain strings or effort objects')
        lifecycle={}
        for key in ('lifecycle','shutdown_date','deprecated_at','retires_at'):
            if isinstance(row.get(key),str):lifecycle[key]=row[key]
        output.append({'provider':provider,'id':mid,'display_name':display,'observed_on':observed_on,
          'capabilities':caps,'reported_limits':limits,'generation_methods':methods,'reasoning_efforts':efforts,
          'lifecycle_metadata':lifecycle,'evidence_kind':'imported catalog metadata; runtime behavior unverified',
          'execution_verified':False})
    return output,pending

def load_registry(path):
    if not Path(path).exists():return {'schema_version':1,'providers':{},'models':[]}
    data=read(path)
    if not isinstance(data,dict) or data.get('schema_version')!=1 or not isinstance(data.get('providers'),dict) or not isinstance(data.get('models'),list):
        raise ValueError('Unsupported model registry; preserve it and use a new file or reviewed migration')
    return data

def import_catalog(path,raw,provider,observed_on,complete=False,items_field=None,id_field=None):
    rows,pending=normalize(raw,provider,observed_on,items_field,id_field)
    if complete and pending:raise ValueError('Pagination indicates more models; cannot claim a complete snapshot')
    data=load_registry(path)
    previous=[m for m in data['models'] if not (complete and m['provider']==provider)]
    merged={(m['provider'],m['id']):m for m in previous}
    merged.update({(m['provider'],m['id']):m for m in rows})
    data['models']=list(merged.values())
    data['providers'][provider]={'observed_on':observed_on,'imported_count':len(rows),
      'completeness':'operator_declared_complete' if complete else 'partial_or_unknown','more_pages_reported':pending}
    data['updated_at']=datetime.now(timezone.utc).isoformat()
    data['policy']='Catalog metadata only. No universal coverage, entitlement, live connection, model execution or benchmark is established.'
    save(path,data)
    return {'imported':len(rows),'provider':provider,'registry':str(path),'total_models':len(data['models']),
      'more_pages_reported':pending,'execution_verified':False}

def check_model(data,provider,model,required,max_age_days=7,today=None):
    if max_age_days<0:raise ValueError('max-age-days must be nonnegative')
    matches=[m for m in data['models'] if m['provider']==provider and m['id']==model]
    base={'provider':provider,'id':model,'execution_verified':False,
      'note':'Metadata assessment only; verify the actual runtime, account access and task-critical behavior before use.'}
    if not matches:return {**base,'decision':'model_not_listed','requirements':{k:'unknown' for k in required}}
    m=matches[0];age=((today or date.today())-date.fromisoformat(m['observed_on'])).days
    stale=age<0 or age>max_age_days
    status={k:('supported' if m['capabilities'].get(k) is True else 'unsupported' if m['capabilities'].get(k) is False else 'unknown') for k in required}
    lifecycle=m.get('lifecycle_metadata',{})
    retired=lifecycle.get('lifecycle') in ('retired','disabled','unavailable')
    for key in ('shutdown_date','retires_at'):
        if lifecycle.get(key):
            try:retired=retired or date.fromisoformat(lifecycle[key][:10])<=(today or date.today())
            except ValueError:pass
    decision='metadata_supported'
    if retired:decision='reported_retired_or_unavailable'
    elif 'unsupported' in status.values():decision='unsupported_requirement'
    elif stale or 'unknown' in status.values() or not required:decision='needs_verification'
    return {**base,'decision':decision,'requirements':status,'stale_or_future_dated':stale,'observed_on':m['observed_on']}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--registry',type=Path,default=registry_path())
    sub=p.add_subparsers(dest='command',required=True)
    q=sub.add_parser('import');q.add_argument('--input',type=Path,required=True);q.add_argument('--provider',required=True)
    q.add_argument('--observed-on',required=True);q.add_argument('--complete',action='store_true');q.add_argument('--items-field');q.add_argument('--id-field')
    q=sub.add_parser('list');q.add_argument('--provider');q.add_argument('--limit',type=int,default=20)
    q=sub.add_parser('check');q.add_argument('--provider',required=True);q.add_argument('--model',required=True)
    q.add_argument('--require',action='append',default=[]);q.add_argument('--max-age-days',type=int,default=7)
    a=p.parse_args()
    if a.command=='import':result=import_catalog(a.registry,read(a.input),a.provider,a.observed_on,a.complete,a.items_field,a.id_field)
    else:
        data=load_registry(a.registry)
        if a.command=='check':result=check_model(data,a.provider,a.model,a.require,a.max_age_days)
        else:
            if not 1<=a.limit<=100:raise ValueError('limit must be 1..100')
            rows=[m for m in data['models'] if not a.provider or m['provider']==a.provider]
            result={'total':len(rows),'shown':min(len(rows),a.limit),'models':rows[:a.limit],
              'coverage':'Imported snapshots only; this is not a worldwide live inventory.'}
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0

if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    try:raise SystemExit(main())
    except (OSError,ValueError,TypeError,KeyError) as e:
        print('smart-agent-models: '+str(e),file=sys.stderr);raise SystemExit(1)
