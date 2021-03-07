#!/usr/bin/python
import subprocess as sub
import optparse
import os
import sys
import platform
import requests
import time
import uuid
from colorama import Fore
from uuid import getnode as get_mac
interfaces = ['eth0','wlan0',]
operating_sys = platform.system()
macdec = get_mac()
original_mac = ':'.join(("%012X" % macdec)[i:i+2] for i in range(0, 12, 2))
wi = "\033[1;37m"  # >>White#
rd = "\033[1;31m"  # >Red   #
gr = "\033[1;32m"  # >Green #
yl = "\033[1;33m"  # >Yellow#
cy = Fore.CYAN
bk = Fore.CYAN
mg = Fore.MAGENTA
path = '/usr/local/lib/python3.8/dist-packages'
tool = print(f'{wi}{yl}MAC {wi}&& {wi}{yl}IP Changer')
owner = print(f'{wi}Made By:{wi}{cy}FonderElite, {wi}{gr}a Cyber-Security Student and a Programmer')
time.sleep(0.5)
try:
    import subprocess
    import optparse
    import uuid
    if uuid and str(requests) in path or sys.modules:
        print(f'{wi}{gr}[+]{wi}No missing dependencies')
    elif uuid  and str(requests) not in path or sys.modules:
        print(f"{wi}Checking modules if are complete...")
        time.sleep(0.5)
        print(f'{wi}{rd}[-]{wi}uuid Module')
        print(f'{wi}{rd}[-]{wi}requests Module')
        os.system('pip install uuid')
        os.system('pip install requests')
        print(f'{wi}Modules Are Set...')
        time.sleep(0.7)
        import uuid
        import requests

    elif requests or uuid not in path or sys.modules :
        print(f'{wi}{rd}[-]{wi}Missing Modules')
except ImportError:
    print(f'{wi}{rd} Missing Modules, Trying to Import')
    print(f'{wi}Checking pip version')
    time.sleep(0.5)
    process = sub.Popen('pip --version', shell=True, stdout = -1, stderr=subprocess.STDOUT)
    out,err = process.communicate()
    if out:
        print(f"Pip version is: {out}")
        print(f'{wi}Installing missing modules using pip...')
        time.sleep(0.5)
        os.system('pip install uuid')
        os.system('pip install requests')
        print(f'{wi}Trying to Import missing modules...')
        time.sleep(0.7)
        import uuid
        import requests
    else:
        print(f"{wi}Try Importing it manually")

def change_mac(interface):
 try:
  mac = input("Input a Mac Address: ")
  print(f"Original Mac Address: {wi}{yl}{original_mac}")
  time.sleep(0.5)
  print(f'{wi}{gr}[+]{wi}Changing MAC for interface {wi}{yl}{interface} {wi} to {wi}{yl}{mac}')
  sub.call(['ifconfig',interface,'down'])
  sub.call(['ifconfig',interface,'hw','ether',mac])
  sub.call(['ifconfig',interface],'up')
 except TypeError:   
  print(wi + rd + "[-]" + wi + "Error")
change_mac("eth0")
                   
