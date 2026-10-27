import importlib.util,json,pathlib,subprocess,sys,tempfile,unittest
from datetime import date

ROOT=pathlib.Path(__file__).resolve().parents[1]/'smart-agent'
spec=importlib.util.spec_from_file_location('portable_models',ROOT/'scripts/models.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
TODAY='2026-10-27'

class ModelCatalogTests(unittest.TestCase):
 def test_common_shapes_and_exact_ids(self):
  for payload,expected in [({'data':[{'id':'anything-v99'}]},'anything-v99'),({'models':[{'slug':'unreleased-synthetic'}]},'unreleased-synthetic'),({'models':[{'name':'models/future-vision'}]},'models/future-vision'),({'models':[{'model':'local:quantized'}]},'local:quantized'),([{'id':'org/repository'}],'org/repository')]:
   with self.subTest(expected=expected):
    rows,pending=m.normalize(payload,'any-provider',TODAY)
    self.assertEqual(rows[0]['id'],expected);self.assertFalse(rows[0]['execution_verified'])

 def test_custom_future_wrapper_and_capability(self):
  rows,_=m.normalize({'results':{'entries':[{'release':{'identifier':'未知/next@v7'},'capabilities':{'future_sensor':True}}]}},'future-vendor',TODAY,'results.entries','release.identifier')
  self.assertEqual(rows[0]['id'],'未知/next@v7');self.assertTrue(rows[0]['capabilities']['future_sensor'])

 def test_provider_namespaces_do_not_collide(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'registry.json'
   for provider in ['one','two']:m.import_catalog(p,{'data':[{'id':'same-name'}]},provider,TODAY)
   self.assertEqual(len(m.load_registry(p)['models']),2)

 def test_partial_preserves_missing_and_complete_replaces_only_provider(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'registry.json'
   m.import_catalog(p,[{'id':'old'},{'id':'keep'}],'one',TODAY)
   m.import_catalog(p,[{'id':'other'}],'two',TODAY)
   m.import_catalog(p,[{'id':'keep'}],'one',TODAY)
   self.assertEqual(len(m.load_registry(p)['models']),3)
   m.import_catalog(p,[{'id':'keep'}],'one',TODAY,complete=True)
   self.assertEqual({(x['provider'],x['id']) for x in m.load_registry(p)['models']},{('one','keep'),('two','other')})

 def test_pagination_prevents_complete_claim_and_writes_nothing(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'registry.json'
   with self.assertRaises(ValueError):m.import_catalog(p,{'data':[{'id':'x'}],'has_more':True},'p',TODAY,complete=True)
   self.assertFalse(p.exists())

 def test_duplicate_ids_reject_without_replacing_good_registry(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'registry.json';m.import_catalog(p,[{'id':'x'}],'p',TODAY);before=p.read_bytes()
   with self.assertRaises(ValueError):m.import_catalog(p,[{'id':'x'},{'id':'x'}],'p',TODAY)
   self.assertEqual(p.read_bytes(),before)

 def test_account_fields_and_arbitrary_objects_are_not_copied(self):
  rows,_=m.normalize({'account':'PRIVATE-MARKER','data':[{'id':'x','api_key':'PRIVATE-MARKER','billing':{'secret':'PRIVATE-MARKER'},'owned_by':'PRIVATE-MARKER'}]},'p',TODAY)
  self.assertNotIn('PRIVATE-MARKER',json.dumps(rows))

 def test_model_name_never_implies_a_capability(self):
  rows,_=m.normalize([{'id':'vision-tools-computer-use-best-pro'}],'p',TODAY)
  result=m.check_model({'models':rows},'p',rows[0]['id'],['computer_use'],today=date(2026,10,27))
  self.assertEqual(result['decision'],'needs_verification');self.assertEqual(result['requirements']['computer_use'],'unknown')

 def test_explicit_non_support_blocks(self):
  rows,_=m.normalize([{'id':'x','capabilities':{'computer_use':False}}],'p',TODAY)
  self.assertEqual(m.check_model({'models':rows},'p','x',['computer_use'],today=date(2026,10,27))['decision'],'unsupported_requirement')

 def test_stale_or_future_observations_need_verification(self):
  for when in ['2020-01-01','2035-01-01']:
   rows,_=m.normalize([{'id':'x','capabilities':{'computer_use':True}}],'p',when)
   self.assertEqual(m.check_model({'models':rows},'p','x',['computer_use'],today=date(2026,10,27))['decision'],'needs_verification')

 def test_declared_support_is_not_execution(self):
  rows,_=m.normalize([{'id':'x','capabilities':{'computer_use':{'supported':True},'effort':{'supported':True,'new_level':{'supported':True}}}}],'p',TODAY)
  result=m.check_model({'models':rows},'p','x',['computer_use'],today=date(2026,10,27))
  self.assertEqual(result['decision'],'metadata_supported');self.assertFalse(result['execution_verified']);self.assertTrue(rows[0]['capabilities']['effort.new_level'])

 def test_invalid_shape_and_capabilities_fail(self):
  for payload in [{'unknown':[]},[{'capabilities':{}}],[{'id':'x','capabilities':{'tools':'yes'}}]]:
   with self.assertRaises(ValueError):m.normalize(payload,'p',TODAY)

 def test_retirement_metadata_blocks_and_limits_do_not_imply_tools(self):
  rows,_=m.normalize([{'id':'x','inputTokenLimit':50000,'supportedGenerationMethods':['generateContent'],'shutdown_date':'2026-10-26','capabilities':{'computer_use':True}}],'p',TODAY)
  self.assertEqual(rows[0]['reported_limits']['input_tokens'],50000)
  self.assertEqual(m.check_model({'models':rows},'p','x',['computer_use'],today=date(2026,10,27))['decision'],'reported_retired_or_unavailable')

 def test_cli_check_does_not_create_registry_or_call_a_provider(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'absent.json'
   r=subprocess.run([sys.executable,str(ROOT/'scripts/models.py'),'--registry',str(p),'check','--provider','unknown','--model','future','--require','new_capability'],capture_output=True,text=True,check=True)
   self.assertEqual(json.loads(r.stdout)['decision'],'model_not_listed');self.assertFalse(p.exists())

if __name__=='__main__':unittest.main()
