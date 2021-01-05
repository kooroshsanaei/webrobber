import os, sys, requests
from colorama import Fore as color
from time import sleep

def clear():
    os.system('clear')



def __start__():
    #Try For Gettin the information
    try:
        sleep(0.1)
        print(color.CYAN+"[!] Enter The Domain\n")
        sleep(0.1)
        site = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"IG"+color.RED+"/"+color.LIGHTYELLOW_EX+"WHOIS"+color.RED+"""]
└──╼ """+color.WHITE+"» ")
        #Send a reqeust with method get from hackertarget api
        data = requests.get('http://api.hackertarget.com/whois/?q='+site).text

        print(color.CYAN+data)
        try:
            input(color.RED+"\n[!] "+color.GREEN+"Back To Menu (Press Enter...)")
        except:
            print("")
            sys.exit()
    except:
        print(color.RED+"\nPlease Enter a Website name...")
        sleep(1)


