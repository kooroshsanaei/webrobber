import requests, sys, os
from time import sleep
from colorama import Fore as color 

def __start__():
    try:
        sleep(0.1)
        print(color.CYAN+"[!] Enter IP‌ Or The Domain\n")
        sleep(0.1)
        site = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"IG"+color.RED+"/"+color.LIGHTYELLOW_EX+"Port-Scaner"+color.RED+"""]
└──╼ """+color.WHITE+"» ")

        print(color.CYAN+"Loading...")
        data = requests.get('https://api.hackertarget.com/nmap/?q='+site).text
        print(color.LIGHTYELLOW_EX+data)

        try:
            input(color.RED+"\n[!] "+color.GREEN+"Back To Menu (Press Enter...)")
        except:
            print("")
            sys.exit()
    except:
        print(color.RED+"\nSome Thing Went Wrong...")
        sleep(1)