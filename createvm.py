# coding: utf-8
import subprocess
subprocess.call("echo Creating VM ", shell=True)
subprocess.call("echo az vm create --resource-group D05110311_Resources --name VM02 --image UbuntuLTS --generate-ssh-keys --output json",shell=True)
subprocess.call("az vm create --resource-group D05110311_Resources --name VM02 --image UbuntuLTS --generate-ssh-keys --output json",shell=True)
