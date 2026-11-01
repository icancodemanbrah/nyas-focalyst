from pathlib import Path
import json,zipfile
p=Path(__file__).resolve().parent;out=p/'deliverables';out.mkdir(exist_ok=True)
html=(p/'index.html').read_text().replace('<link rel="stylesheet" href="theme.css">','<style>'+(p/'theme.css').read_text()+'</style>').replace('<script src="simulation.js"></script>','<script>'+(p/'simulation.js').read_text()+'</script>').replace('<script src="app.js"></script>','<script>'+(p/'app.js').read_text()+'</script>')
(out/'Focalyst.html').write_text(html)
scm={'authURL':['ai2.appinventor.mit.edu'],'YaVersion':'232','Source':'Form','Properties':{'$Name':'Screen1','$Type':'Form','$Version':'31','AppName':'Focalyst','Title':'Focalyst','TitleVisible':'False','Sizing':'Responsive','Scrollable':'False','Uuid':'0','$Components':[{'$Name':'WebViewer1','$Type':'WebViewer','$Version':'13','Height':'-2','Width':'-2','HomeUrl':'http://localhost/Focalyst.html','UsesLocation':'False','Uuid':'1'}]}}
with zipfile.ZipFile(out/'Focalyst.aia','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('assets/Focalyst.html',html)
 z.writestr('src/appinventor/ai_demo/Focalyst/Screen1.scm','#|\n$JSON\n'+json.dumps(scm)+'\n|#')
 z.writestr('src/appinventor/ai_demo/Focalyst/Screen1.bky','<xml xmlns="https://developers.google.com/blockly/xml"><yacodeblocks ya-version="232" language-version="36"></yacodeblocks></xml>')
 z.writestr('youngandroidproject/project.properties','main=appinventor.ai_demo.Focalyst.Screen1\nname=Focalyst\nassets=../assets\nsource=../src\nbuild=../build\nversioncode=1\nversionname=1.0\nuseslocation=False\n')
# Package only the current implementation and its documentation/tests.
with zipfile.ZipFile(out/'Focalyst-source.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in ['index.html','theme.css','app.js','simulation.js','package-demo.py']:
  z.write(p/name,name)
 for f in (p/'tests').iterdir():
  if f.suffix in {'.cjs','.py'}: z.write(f,str(f.relative_to(p)))
 for name in ['README.md','METHODOLOGY.md','VALIDATION.md','simulation-results.json','test-results.json','Focalyst.html']:
  if (out/name).exists(): z.write(out/name,'deliverables/'+name)
with zipfile.ZipFile(out/'Focalyst.aia') as z:
 assert z.testzip() is None
 assert z.read('assets/Focalyst.html')==(out/'Focalyst.html').read_bytes()
