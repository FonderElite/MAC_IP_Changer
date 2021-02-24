import os
from colorama import Fore as Fr
import importlib
import time
import module_name
import subprocess as sub
wi = "\033[1;37m"  # >>White#
rd = "\033[1;31m"  # >Red   #
gr = "\033[1;32m"  # >Green #
yl = "\033[1;33m"  # >Yellow#
cy = Fr.CYAN
bk = Fr.CYAN
mg = Fr.MAGENTA
dep = ['requests','uuid']
run = os.system
mod_loc = '/lib/python3/dist-packages'
try:
    import module_name
except ImportError:
    print(f"{wi} {gr}[+]Pip installing module_name automatically")
    time.sleep(0.5)
    run('pip install module_name')
    print(f'{wi}Importing module_name...')
    time.sleep(0.5)
    import module_name

def check():
     print(f'{wi}Checking for some missing dependencies...')
     if dep[0] and dep[1] not in mod_loc:
         print(f'{wi}{rd}[-]{wi}You have some missing dependencies')
while True:
 choice = input(wi + gr + '[+]Install' + wi +  ' tor.py? or mac.py (tor/mac): ')
 if str(choice) =='tor' or str(choice)=='Tor':
    run('chmod 777 autoTOR.py')
    run('mkdir /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/autoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/autoTOR.py')
    print('''\n\nCongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
 if str(choice) == 'mac' or str(choice) == 'Mac':
     perm = run('chmod +x 777 macc.py')
     process = sub.Popen('pip --version', shell=True, stdout=-1, stderr=sub.STDOUT)
     out, err = process.communicate()
     modules = help('modules')
     check()



