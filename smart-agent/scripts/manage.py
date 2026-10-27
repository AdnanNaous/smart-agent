#!/usr/bin/env python3
"""SMART AGENT local module management. No model calls, dispatch, or background jobs."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'

def codex_home():
    return Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')).expanduser()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)

def state_path():
    override = os.environ.get('SMART_AGENT_STATE')
    return Path(override) if override else codex_home() / 'skill-state/smart-agent/modules.json'

def registry():
    data = read(ASSETS / 'modules.json')
    states = read(state_path()) if state_path().exists() else {}
    return [{**m, 'enabled': states.get(m['id'], m.get('default_enabled', True))} for m in data['modules']]

def recommend(query, limit=5):
    terms = set(re.findall(r'[\w.]+', query.casefold()))
    found = []
    for m in registry():
        if not m['enabled']:
            continue
        words = set(re.findall(r'[\w.]+', ' '.join([m['id'],m['title'],*m['keywords']]).casefold()))
        hits = sorted(terms & words)
        if hits:
            found.append({'id':m['id'], 'title':m['title'], 'reference':m['reference'], 'matched':hits, 'score':len(hits)})
    return sorted(found, key=lambda m:(-m['score'],m['id']))[:limit]

def refresh_models(catalog, surfaces, output):
    raw = read(catalog)
    models = raw.get('models')
    if not isinstance(models,list):
        raise ValueError('Catalog must contain a models list')
    surface = read(surfaces) if surfaces else {'observed_on':None,'surfaces':{}}
    rows=[]
    for m in models:
        name=m.get('slug') or m.get('id')
        if not isinstance(name,str) or not name:
            raise ValueError('Catalog model is missing a string slug/id')
        efforts=m.get('supported_reasoning_levels',[])
        rows.append({'id':name,'display_name':m.get('display_name',name),
          'visibility':m.get('visibility','unknown'),
          'local_catalog_efforts':[v.get('effort') if isinstance(v,dict) else v for v in efforts],
          'surface_support':{k:v[name] for k,v in surface.get('surfaces',{}).items() if name in v}})
    if len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Duplicate model IDs in catalog')
    data={'schema_version':2,'refreshed_at':datetime.now(timezone.utc).isoformat(),
      'catalog_fetched_at':raw.get('fetched_at'),'catalog_sha256':hashlib.sha256(Path(catalog).read_bytes()).hexdigest(),
      'surface_observed_on':surface.get('observed_on'),'models':rows,
      'policy':'Inventory only. Cache presence is not live permission or availability. Recheck the exact target schema before routing; preserve the user-selected coordinator and effort. No prices or rankings inferred.'}
    write(output,data)
    return {'models':len(rows),'output':str(output),'surface_observed_on':surface.get('observed_on')}

def token_report(path):
    raw=read(path)
    runs=raw.get('runs',[])
    if not runs:
        return {'calculable':False,'reason':'No measured runs supplied; savings are not calculable.'}
    results=[]
    for r in runs:
        base=r.get('baseline_input_tokens'); actual=r.get('actual_input_tokens')
        valid=lambda n:isinstance(n,(int,float)) and not isinstance(n,bool) and math.isfinite(n) and n>=0
        if not valid(base) or base==0 or not valid(actual):
            raise ValueError('Need positive measured baseline_input_tokens and nonnegative actual_input_tokens')
        quality=r.get('same_task') is True and r.get('quality_passed') is True
        results.append({'id':r.get('id'),'input_tokens_saved':base-actual,
          'input_savings_percent':round(100*(base-actual)/base,2),'quality_validated':quality,
          'accepted_savings_claim':quality,
          'note':'Input-token comparison only. Does not infer billing, cache discounts, output/reasoning tokens or latency.'})
    return {'calculable':True,'runs':results}

def doctor():
    modules=registry(); ids=[m['id'] for m in modules]; errors=[]
    if len(ids)!=len(set(ids)): errors.append('Duplicate module IDs')
    for m in modules:
        p=(ROOT/m['reference']).resolve()
        if not p.is_relative_to(ROOT.resolve()) or not p.is_file(): errors.append('Invalid reference: '+m['id'])
        for dep in m.get('related',[]):
            if dep not in ids: errors.append('Unknown related module: '+dep)
    manifest=read(ASSETS/'toolkit-sources.json')
    missing=[]
    for s in manifest['sources']:
        root=Path(s['root'].replace('${CODEX_HOME}',str(codex_home()))).expanduser()
        if not root.is_dir(): missing.append(s['id'])
    return {'ok':not errors,'modules':len(modules),'enabled':sum(m['enabled'] for m in modules),
      'errors':errors,'missing_optional_sources':missing,
      'scope':'Module references and source presence only. Run toolkit.py check for pins/hashes. No upstream software, accounts, graphics or services exercised.'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('list'); sub.add_parser('doctor')
    q=sub.add_parser('recommend'); q.add_argument('query'); q.add_argument('--limit',type=int,default=5)
    for name in ('show','enable','disable'):
        q=sub.add_parser(name); q.add_argument('module')
    q=sub.add_parser('refresh-models'); q.add_argument('--catalog',type=Path,default=codex_home()/'models_cache.json')
    q.add_argument('--surfaces',type=Path); q.add_argument('--output',type=Path,default=ASSETS/'model-candidates.json')
    q=sub.add_parser('token-report'); q.add_argument('measurements',type=Path)
    a=p.parse_args()
    if a.command=='list': result=registry()
    elif a.command=='doctor':
        result=doctor(); print(json.dumps(result,indent=2,ensure_ascii=False)); return int(not result['ok'])
    elif a.command=='recommend':
        if not 1<=a.limit<=30: raise ValueError('--limit must be 1..30')
        result={'advisory_only':True,'query':a.query,'modules':recommend(a.query,a.limit),
          'fallback':'Use native judgment if no match. This lexical helper never dispatches tools, starts agents, installs software, or chooses a model.'}
    elif a.command in ('show','enable','disable'):
        matches=[m for m in registry() if m['id']==a.module]
        if not matches: raise ValueError('Unknown module ID')
        result=matches[0]
        if a.command!='show':
            states=read(state_path()) if state_path().exists() else {}
            states[a.module]=a.command=='enable'; write(state_path(),states)
            result={**result,'enabled':states[a.module],'state_file':str(state_path())}
    elif a.command=='refresh-models': result=refresh_models(a.catalog,a.surfaces,a.output)
    else: result=token_report(a.measurements)
    print(json.dumps(result,indent=2,ensure_ascii=False)); return 0

if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,TypeError) as e:
        print('smart-agent: '+str(e),file=sys.stderr); raise SystemExit(1)
