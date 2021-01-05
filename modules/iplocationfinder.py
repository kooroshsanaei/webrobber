import requests, sys, os, ipapi
from time import sleep
from colorama import Fore as color


def __start__():
    sleep(0.1)
    print(color.CYAN+"[!] Enter IP Address\n")
    sleep(0.1)
    site = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"IG"+color.RED+"/"+color.LIGHTYELLOW_EX+"IP-Location"+color.RED+"""]
└──╼ """+color.WHITE+"» ")

    data = ipapi.location(ip=site, key=None)
    try:
        print(color.GREEN+"[!] "+color.CYAN+"Here is your Information: ")
        print(color.GREEN+"[!] "+color.RED+"IP => "+data['ip'])
        print(color.GREEN+"[!] "+color.RED+"IP-Version => "+data['version'])
        print(color.GREEN+"[!] "+color.RED+"Country => "+data['country_name'])               
        print(color.GREEN+"[!] "+color.RED+"Calling-Code => "+data['country_calling_code'])
        print(color.GREEN+"[!] "+color.RED+"Region => "+data['region'])
        print(color.GREEN+"[!] "+color.RED+"City => "+data['city']) 
        print(color.GREEN+"[!] "+color.RED+"DNS => "+data['org'])
        try:
            input(color.RED+"\n[!] "+color.GREEN+"Back To Menu (Press Enter...)")
        except:
            print("")
            sys.exit()
    except:
        print(color.RED+"\nPlease Enter IP‌ Address...")
        sleep(1)
