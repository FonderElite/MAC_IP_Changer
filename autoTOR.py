# -*- coding: utf-8 -*-
import sys
import time
import os
import subprocess
import socket
import socks
from colorama import Fore
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
def first_slow_print(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
        time.sleep(2)

def second_slow_print(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
        time.sleep(2)

def third_slow_print(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)


try:
    if os.path.exists('/usr/bin/pip') and os.path.exists('/usr/sbin/tor'):
       pass
    else:
       print(wi +  gr + "[+] " + wi + "Updating...")
       os.system('sudo apt update -y')
       third_slow_print(wi + rd + '[-]' + wi + 'pip is not installed!') 
       third_slow_print(wi + yl + '[!]' + wi + 'Installing pip....')
       subprocess.call(['sudo','apt','install','python3-pip','-y'])
       subprocess.call(['sudo','apt','install','tor','-y'])
except subprocess.CalledProcessError:
    first_slow_print(wi + yl + "[!]" + wi + "pip3 is not installed")
    second_slow_print(wi + yl + "[-]" + wi + "Installing pip...") 
    time.sleep(0.5)
    update = subprocess.check_output('sudo apt update',shell=True)
    pip = subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print(wi + gr +'[+]' + wi + ' pip3 installed succesfully')



try:

    import requests
except Exception:
    print(wi + rd + '[-]' + wi + ' python3 requests is not installed')
    print(os.system('pip3 install requests'))
    os.system('pip3 install requests[socks]')
    print(wi + yl + '[!]' +  wi +'python3 requests is installed ')

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint(wi + yl + "[!]" + wi + "Checking If Tor is Installed......")
time.sleep(2)
try:
    check_tor = subprocess.check_output('which tor', shell=True)
    os.path.exists('/usr/sbin/tor') 
    print(wi + gr + '[+]'+ wi + 'Tor is installed')
except subprocess.CalledProcessError:
    print(wi + rd + '[-]' +  wi + ' Tor is not installed !')
    os.system('sudo apt install tor -y')
    location = os.system('which tor')
    os.path.exists('/usr/sbin/tor')
    print(wi + gr + '[+]' + wi + ' Tor is installed succesfully!')
    print(wi + gr + "Tor location:" +  wi + str(location))


os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print (wi + gr + '[+]' + wi +  'Your IP has been Changed to : '+str(ma_ip()))
print(wi + Fore.MAGENTA + '''\n
                  ~                                                
                   /~      
             \  \ /**     
              \ ////     
              // //
             // //        
           ///&//        
          / & /\ \       
        /  & .,,  \     
      /& %  :       \            
    /&  %   :  ;     `\                                              
   /&' &..%   !..    `.\                                             
  /&' : &''" !  ``. : `.\                                            
 /#' % :  "" * .   : : `.\                                           
I# :& :  !"  *  `.  : ::  I                                          
I &% : : !%.` '. . : : :  I                                          
I && :%: .&.   . . : :  : I                                          
I %&&&%%: WW. .%. : :     I                                          
 \&&&##%%%`W! & '  :   ,'/                                           
  \####ITO%% W &..'  #,'/                                            
    \W&&##%%&&&&### %./                                              
      \###j[\##//##}/                                                
         ++///~~\//_                                                 
          \\ \ \ \  \_                                               
          /  /    \    
''')
print(wi + yl +  "Github:" + wi + " https://github.com/FonderElite")

os.system("service tor start")




time.sleep(3)
print(wi + gr + "[+]" + wi + "Changed your  SOCKETS to 127.0.0.1:9050")
os.system("service tor start")
x = input(wi + gr + "[+]" + wi + 'time to change Ip in Sec [type=60] >> ')
lin = input(wi + gr + '[+]' + wi + 'how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>')
if int(lin) ==int(0):

        while True:
                try:
                        time.sleep(int(x))
                        change()
                except KeyboardInterrupt:

                        print(wi + rd + '\n[-]' + wi +'Auto tor is closed ')
                        quit()

else:
        for i in range(int(lin)):
                    time.sleep(int(x))
                    change()

