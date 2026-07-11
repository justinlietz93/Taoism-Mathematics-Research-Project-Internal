from pathlib import Path
import os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
env=os.environ.copy()
env['PYTHONDONTWRITEBYTECODE']='1'
env['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'
subprocess.run([sys.executable,str(ROOT/'scripts'/'20260711T162758_generate.py')],check=True,env=env)
subprocess.run([sys.executable,str(ROOT/'scripts'/'20260711T162758_run_controls.py'),str(ROOT),'--record'],check=True,env=env)
print('Rebuilt deterministic scientific tables and corruption-control evidence.')
print('The source and executed notebooks are sealed no-I/O evidence artifacts.')
