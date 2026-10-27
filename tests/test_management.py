import importlib.util,json,os,pathlib,subprocess,tempfile,unittest
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1]/'smart-agent'
spec=importlib.util.spec_from_file_location('smart_management',ROOT/'scripts/manage.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
tspec=importlib.util.spec_from_file_location('smart_toolkit',ROOT/'scripts/toolkit.py')
t=importlib.util.module_from_spec(tspec);tspec.loader.exec_module(t)

class ManagementTests(unittest.TestCase):
 def test_disable_changes_recommendations_without_bundle_mutation(self):
  before=(ROOT/'assets/modules.json').read_bytes()
  with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'SMART_AGENT_STATE':str(pathlib.Path(tmp)/'state.json')}):
   self.assertTrue(any(x['id']=='web-3d' for x in m.recommend('threejs')))
   m.write(m.state_path(),{'web-3d':False})
   self.assertEqual(m.recommend('threejs'),[])
   m.write(m.state_path(),{'web-3d':True})
   self.assertTrue(m.recommend('threejs'))
  self.assertEqual((ROOT/'assets/modules.json').read_bytes(),before)

 def test_recommendation_is_bounded_and_does_not_require_known_model(self):
  self.assertLessEqual(len(m.recommend('game assets 3d animation testing',2)),2)
  self.assertEqual(m.recommend('unmatchedxyz987'),[])

 def test_future_models_are_discovered_without_copying_identity(self):
  with tempfile.TemporaryDirectory() as d:
   d=pathlib.Path(d);catalog=d/'cache.json';out=d/'snapshot.json';surfaces=d/'surfaces.json'
   m.write(catalog,{'identity':'PRIVATE-TEST-MARKER','fetched_at':'2027-01-01','models':[{'slug':'future-model-id','supported_reasoning_levels':[{'effort':'new-effort'}],'secret':'PRIVATE-TEST-MARKER'}]})
   m.write(surfaces,{'observed_on':'2026-01-01','surfaces':{'test_surface':{'future-model-id':['new-effort']}}})
   m.refresh_models(catalog,surfaces,out);data=m.read(out)
   self.assertEqual(data['models'][0]['id'],'future-model-id')
   self.assertEqual(data['models'][0]['local_catalog_efforts'],['new-effort'])
   self.assertEqual(data['surface_observed_on'],'2026-01-01')
   self.assertNotIn('PRIVATE-TEST-MARKER',out.read_text())

 def test_no_measurements_means_no_savings_claim(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'usage.json';m.write(p,{'runs':[]})
   self.assertFalse(m.token_report(p)['calculable'])

 def test_savings_requires_quality_and_can_be_negative(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'usage.json';m.write(p,{'runs':[{'baseline_input_tokens':100,'actual_input_tokens':120,'same_task':True,'quality_passed':False}]})
   row=m.token_report(p)['runs'][0]
   self.assertEqual(row['input_savings_percent'],-20)
   self.assertFalse(row['accepted_savings_claim'])

 def test_invalid_usage_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'usage.json'
   for value in [0,-1,True,'100',float('inf')]:
    m.write(p,{'runs':[{'baseline_input_tokens':value,'actual_input_tokens':10}]})
    with self.assertRaises(ValueError):m.token_report(p)

 def test_source_traversal_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(ValueError):t.source_path({'root':d},'../outside')

 def test_portable_source_root(self):
  with tempfile.TemporaryDirectory() as d,patch.dict(os.environ,{'CODEX_HOME':d}):
   self.assertEqual(t.expanded_root('${CODEX_HOME}/sources').resolve(),(pathlib.Path(d)/'sources').resolve())

 def test_changed_indexed_content_fails_integrity(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'guide.md';p.write_text('original');original=t.sha256(p);p.write_text('changed')
   source={'id':'test','root':d,'license_files':[]}
   entry={'source':'test','path':'guide.md','id':'test:guide.md','sha256':original}
   result,code=t.check({'sources':[source]},{'entries':[entry]})
   self.assertEqual(code,1);self.assertIn('Content differs',result['errors'][0])

 def test_optional_missing_attachment_is_reported_without_false_verification(self):
  result,code=t.check({'sources':[],'attachment':{'path':'unlikely-missing-file-xyz','sha256':'none','optional':True}},{'entries':[]})
  self.assertEqual(code,0);self.assertEqual(len(result['warnings']),1)

if __name__=='__main__':unittest.main()
