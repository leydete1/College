import subprocess
subprocess.call("$origin=leydete1@LAPTOP-TLLPGO6J:~/flaskproject/flaskprojectenv/College", shell=True)
subprocess.call("echo Listing repository files" , shell=True)
subprocess.call("ls -ltr $origin", shell=True)
subprocess.call("echo Adding files to repository" , shell=True)
subprocess.call("git add ." , shell=True)
subprocess.call("echo Commiting repository" , shell=True)
subprocess.call("git commit -m \"Sorce upload \"" , shell=True)
1
