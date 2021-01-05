''' 
Creator => ZeroDey
Telegram Channel => Zeroo_Dey
YouTube => TheZeroDey
Telegram =>zerodey
Email => sshprotokzd@gmail.com

Version => 1.0 , 2021
This Toll has writen by Zerodey in 2021 and it will have More updates on it 
and soon i will add more thins to it like HoneyPot Detector and Proxy changer,
and more....


One more thing, I DO NOT have any responsiblity from your illegal uses.

Have Fun 
             _______  _______   _______   _______   ______    _______          
            / ___   ) (  ____ \ (  ____ ) (  ___  ) (  __  \  (  ____ \ |\     /|
            \/   )  | | (    \/ | (    )| | (   ) | | (  \  ) | (    \/ ( \   / )
                /   ) | (__     | (____)| | |   | | | |   ) | | (__      \ (_) / 
               /   /  |  __)    |     __) | |   | | | |   | | |  __)      \   /  
              /   /   | (       | (\ (    | |   | | | |   ) | | (          ) (   
             /   (_/\ | (____/\ | ) \ \__ | (___) | | (__/  ) | (____/\    | |   
            (_______/ (_______/ |/   \__/ (_______) (______/  (_______/    \_/   
                                                                               ,Product


'''
import os, sys
from time import sleep 
from menu import menu
from Classes import myClasses
def clear():
    os.system('clear')
from modules import wordpress, cmsdetect ,cloudflare,iplocationfinder, whois, admin_finder, port_scan, dnslookup



myClasses.Introduce()

def install_module(module):
    os.system('clear')
    print(color.RED+"""\n Please Install"""+ module +"""colorama\n 
    pip3 install colorama\n
    in windows pip install colorama""")
    sleep(3)



# Check for needed modules

#1 Colorama
try:
    from colorama import Fore as color
except:
    install_module('colorama')

#2 Requests
try:
    import requests
except:
    install_module('Requests')

#3 IPapi
try:
    import ipapi
except:
    install_module('IPapi')

#4 BuiltWith
try:
    import builtwith
except:
    install_module('BuiltWith')



#Lets Have some FuN

while True:

    try:
        menu.banner()
        menu.main_menu()
#Get input from the user for going through menu options
        option = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/" """]
└──╼ """+color.WHITE+"» ")
        
        #IF‌ option == 1 go to IG‌
        
        if (option == '1'):
            clear()
            menu.banner()
            menu.info_gathering()
            inside_option = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"IG"+color.RED+"""]
└──╼ """+color.WHITE+"» ")
#Check if option is 1 from information gathering  go to IP‌ location
            if (inside_option == '1'):
                clear()
                try:
                    iplocationfinder.__start__()
                except:
                    print("")
                    sys.exit

#CHECK‌ if option is 2 from IG‌ go to who is 
            elif (inside_option == '2'):
                clear()
                try:
                    menu.banner()
                    whois.__start__()
                except:
                    print("")
                    sys.exit

#Check if inside option is 3 from IG‌ go to Admin Finder            
            elif (inside_option == '3'):
                clear()
                try:
                    menu.banner()
                    admin_finder.__start__()
                except:
                    print("")
                    sys.exit

#Check if inside option is 4 From IG‌ go to port scanner
            elif (inside_option == '4'):
           
                clear()
                try:
                    menu.banner()
                    port_scan.__start__()
                except:
                    print("Something went wrong")
                    sys.exit()

#Check if inside option is 5 from IG‌ go to DNS-LookUp
            elif (inside_option == '5'):
                clear()
                try:
                    menu.banner()
                    dnslookup.__start__()
                except:
                    print(color.RED+"Something went Wrong")
                    sys.exit()

#Check if inside option is 6 from IG‌ go to Robots Scanner
            elif (inside_option == '6'):
                clear()
                try:
                    menu.banner()
                    robotscaner.__start__()
                except:
                    print(color.RED+"Something Went‌ Wrong...")
                    sys.exit()

#Check if inside option is 7 from IG‌ go to Cloudflare bypasser
            elif (inside_option == '7'):

                clear()
                try:
                    menu.banner()
                    cloudflare.__start__()
                except:
                    print(color.RED+"Something went Wrong....")
                    sys.exit()

#check if inside option is 8 from IG go to cms-detection
            elif (inside_option == '8'):
                clear()
                try:
                    menu.banner()
                    cmsdetect.__start__()
                except:
                    print(color.RED+"Somethingbad happend")
                    sleep(1)
                    sys.exit()

#check if inside option is 9 From IG Back to the menu
            elif (inside_option == '9'):
                pass

        elif (option == '2'):
            clear()
            menu.banner()
            menu.cms_robber()
            cms_inside_option = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"Cms"+color.RED+"""]
└──╼ """+color.WHITE+"» ")
            if (cms_inside_option == '1'):
                clear()
                menu.banner()
                menu.infowp()
                wp_inside_option = input(color.RED+"┌─["+color.LIGHTGREEN_EX+"WebRobber"+color.RED+"/"+color.WHITE+"Home"+color.RED+"/"+color.CYAN+"Cms"+color.RED+'/'+color.LIGHTYELLOW_EX+'Wordpress'+"""]
└──╼ """+color.WHITE+"» ")
                if (wp_inside_option == '1'):
                    clear()
                    try:
                        menu.banner()
                        wordpress.wpplug()
                    except:
                        print(color.RED+"Something bad happend....")
                        sys.exit()
                elif (wp_inside_option == '2'):
                    clear()
                    try:
                        menu.banner()
                        wordpress.user_finder()
                    except:
                        print(color.RED+"Something bad happend....")
                        sys.exit
                elif (wp_inside_option == '3'):
                    sys.exit()
        
        elif (option == '3'):
            clear()

            try:
                menu.pdeveloper()

            except:
                print(color.RED+"Something bad happend....")
                sys.exit()

#Check if option is 4 Then Exit from the program
        elif (option == '4'):
            print("Thank's for being here...");sleep(1.8);clear()
            break

    except:
        os.system('clear')
        print(color.RED+"Something bad happend....\n"+"""
        Mabye You dont have Required Modules in the requirements.txt file,Check it out\n""")
        sleep(3)
        sys.exit()



'''
             _______  _______   _______   _______   ______    _______          
            / ___   ) (  ____ \ (  ____ ) (  ___  ) (  __  \  (  ____ \ |\     /|
            \/   )  | | (    \/ | (    )| | (   ) | | (  \  ) | (    \/ ( \   / )
                /   ) | (__     | (____)| | |   | | | |   ) | | (__      \ (_) / 
               /   /  |  __)    |     __) | |   | | | |   | | |  __)      \   /  
              /   /   | (       | (\ (    | |   | | | |   ) | | (          ) (   
             /   (_/\ | (____/\ | ) \ \__ | (___) | | (__/  ) | (____/\    | |   
            (_______/ (_______/ |/   \__/ (_______) (______/  (_______/    \_/   
                                                                               ,Product



'''