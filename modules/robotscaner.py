import requests, sys,os
from colorama import Fore as color 
from time import sleep

search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']




def __start__():

    try:
        sleep(0.1)
        print(color.CYAN+"[!] Enter The Domain\n")
        sleep(0.1)
        site = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"IG"+color.RED+"/"+color.LIGHTYELLOW_EX+"Robots-Scaner"+color.RED+"""]
└──╼ """+color.WHITE+"» ")
        print(color.CYAN+"Loading...")

        if ("http" in site):
            pass
        elif ('http' != site):
            site = ('http://'+site)

        for target in search:
            sleep(0.1)
            
            new_url = (site+'/'+target)
            data = requests.get(new_url)

            if (data.status_code == 200 or data.status_code == 405):
                print(color.GREEN+" [+] "+new_url+ " Found")
            else:
                print(color.RED+" [-] "+new_url+ " Not Found")
        try:
            input(color.RED+"\n[!] "+color.GREEN+"Back To Menu (Press Enter...)")
        except:
            print("")
            sys.exit()
    except:
        print(color.RED+"\nSomething Went Wrong...")
        sleep(1)

__start__()