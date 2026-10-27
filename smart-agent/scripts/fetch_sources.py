#!/usr/bin/env python3
"""Explicitly acquire one pinned source as inert sparse reference material."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from toolkit import ASSETS, expanded_root

def fetch(source, destination=None):
    revision=source.get('revision','')
    if not re.fullmatch(r'[0-9a-f]{40}',revision):
        raise ValueError('Source has no exact Git revision; use its separately documented installer')
    target=Path(destination) if destination else expanded_root(source['root'])
    if target.exists():
        raise ValueError('Destination already exists. Preserve it; use a new reviewed destination instead.')
    if not source['url'].startswith('https://') or not source['url'].endswith('.git'):
        raise ValueError('Only recorded HTTPS Git sources are supported')
    git=shutil.which('git')
    if not git: raise ValueError('Git is required')
    target.parent.mkdir(parents=True,exist_ok=True)
    # Initialize without checkout; fetch only the pin, then select inert documents.
    subprocess.run([git,'init',str(target)],check=True,capture_output=True,timeout=30)
    subprocess.run([git,'-C',str(target),'remote','add','origin',source['url']],check=True,timeout=30)
    subprocess.run([git,'-C',str(target),'fetch','--depth','1','--filter=blob:none','origin',revision],check=True,timeout=300)
    subprocess.run([git,'-C',str(target),'sparse-checkout','init','--no-cone'],check=True,timeout=30)
    paths=['/'+x['pattern'] for x in source['catalog']]+['/'+x for x in source.get('license_files',[])]
    subprocess.run([git,'-C',str(target),'sparse-checkout','set','--no-cone',*paths],check=True,timeout=30)
    subprocess.run([git,'-C',str(target),'-c','core.hooksPath='+str(target/'.git/no-hooks'),'checkout','--detach',revision],check=True,timeout=300)
    actual=subprocess.check_output([git,'-C',str(target),'rev-parse','HEAD'],text=True,timeout=30).strip()
    if actual!=revision: raise ValueError('Checkout revision mismatch')
    return {'id':source['id'],'revision':actual,'destination':str(target),'executed_upstream_code':False,
      'next':'Review documents and licenses. For an overridden destination update the manifest root deliberately before offline index refresh.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',required=True);p.add_argument('--destination',type=Path)
    a=p.parse_args();manifest=json.loads((ASSETS/'toolkit-sources.json').read_text(encoding='utf-8'))
    matches=[s for s in manifest['sources'] if s['id']==a.source]
    if not matches: raise ValueError('Unknown source ID')
    print(json.dumps(fetch(matches[0],a.destination),indent=2));return 0
if __name__=='__main__':
    try: raise SystemExit(main())
    except (OSError,ValueError,subprocess.SubprocessError) as e:
        print('fetch-sources: '+str(e),file=sys.stderr);raise SystemExit(1)
