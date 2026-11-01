from pathlib import Path
import subprocess,json,datetime,sys
root=Path(__file__).resolve().parent.parent
results=[]
for script in ['engine.cjs','stream.cjs','simple-browser.cjs','simple-edge-browser.cjs']:
    command=['node',str(root/'tests'/script)]
    run=subprocess.run(command,cwd=root,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
    results.append({'test':script,'exit_code':run.returncode,'output':run.stdout})
    report={'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':results}
    (root/'deliverables'/'test-results.json').write_text(json.dumps(report,indent=2))
    print(run.stdout,flush=True)
    if run.returncode:sys.exit(run.returncode)
print('All four validation suites passed.',flush=True)
