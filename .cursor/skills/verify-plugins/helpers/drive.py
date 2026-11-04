#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,tempfile,shutil,sys,hashlib
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'artifacts/verification';OUT.mkdir(parents=True,exist_ok=True)
scratch=Path(tempfile.mkdtemp(prefix='verify-plugin-cli-'));proof={'scope':'Actual shipped plugin CLI and missing-folder user path in isolated source copy; separate existing mocked unit tests. Not a C++ chat application.','passed':False}
try:
 for name in ['main.py','plugin_interface.py']:shutil.copy2(ROOT/name,scratch/name)
 shutil.copytree(ROOT/'plugins',scratch/'plugins',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 shutil.copytree(ROOT/'tests',scratch/'tests',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 def run(args):
  p=subprocess.run([sys.executable,'-B']+args,cwd=scratch,capture_output=True,text=True,timeout=15)
  return {'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 proof['sourceSha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'main.py',ROOT/'plugin_interface.py']}
 proof['doctor']=run(['-c',"import ast,pathlib;[ast.parse(p.read_text()) for p in pathlib.Path('.').rglob('*.py')]"])
 assert proof['doctor']['exit']==0,'Syntax doctor failed'
 proof['normal']=run(['main.py']);x=proof['normal']
 assert x['exit']==0 and x['stderr']=='','CLI exited with error'
 for text in ['2 plugin(s) loaded.','Executing PluginOne: Hello from the first plugin!','Executing PluginTwo: Greetings from the second plugin!','Application finished.']:assert text in x['stdout'],'Missing real output: '+text
 (scratch/'plugins').rename(scratch/'plugins-off')
 proof['missingFolder']=run(['main.py']);x=proof['missingFolder']
 assert x['exit']==0 and "Plugin folder 'plugins' not found." in x['stdout'] and 'No plugins were loaded' in x['stdout'],'Missing-folder handling failed'
 (scratch/'plugins-off').rename(scratch/'plugins')
 proof['existingUnitTests']=run(['-m','unittest','discover','-v']);assert proof['existingUnitTests']['exit']==0,'Existing unit suite failed'
 assert not (scratch/'plugins/faulty_plugin_for_test.py').exists(),'Existing unit test left faulty plugin'
 proof['passed']=True
except Exception as e:proof['failure']=str(e)
finally:
 (OUT/'plugins.json').write_text(json.dumps(proof,indent=2)+'\n');shutil.rmtree(scratch);assert (OUT/'plugins.json').exists();print(json.dumps(proof,indent=2))
if not proof['passed']:raise SystemExit(1)
