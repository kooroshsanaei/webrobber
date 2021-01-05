import requests, builtwith, sys
from colorama import Fore as color
from time import sleep


def __start__():
    try:
        sleep(0.1)
        print(color.CYAN+"[!] Enter The Domain\n")
        sleep(0.1)
        site = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"IG"+color.RED+"/"+color.LIGHTYELLOW_EX+"Cms-Detect"+color.RED+"""]
└──╼ """+color.WHITE+"» ")

        if not 'https://' in site or not 'http://' in site:
            site = ("http://"+site)

        print(color.CYAN+"Loading...")
        info = builtwith.parse(site)

        for name in info:
            value = ''
            for val in info[str(name)]:
                name = name.replace('-',' ');name = name.title()
                value += str(val)
                print(color.BLUE+'\n'+name+': '+ value)

        try:
            input(color.GREEN+" [*] Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()

    except:
        print(color.RED+"Something bad happend...")
        sleep(1)
        sys.exit()

