import os
import sys
import subprocess
here = os.path.dirname(os.path.abspath(__file__))
latest = '%s/data' % here
# Don't continue if we don't have latest folder
if not os.path.exists(latest):
    print('%s does not have parsed data.' % latest)
    sys.exit(0)
print(latest)
folders = []

# r=root, d=directories, f = files
listofdir=os.listdir(latest)
for name in listofdir:
           print(latest) 
           path=os.path.join(latest, name)
           theproc = subprocess.Popen([sys.executable, path+"/"+"scrape.py"])
           theproc.communicate()
           print(path+"/"+"scrap.py")
           theproc = subprocess.Popen([sys.executable, path+"/"+"parse.py"])
           theproc.communicate()
           print(path+"/"+"parse.py")

           theproc = subprocess.Popen([sys.executable, path+"/"+"save.py"])
           theproc.communicate()
           print(path+"/"+"save.py")
        
      