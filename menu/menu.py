import os, sys
from colorama import Fore as color
from time import sleep
def clear():
    os.system('clear')

    
#Create the header menu for the framework


def banner():
    clear()
    print(color.RED+"""
██╗    ██╗███████╗██████╗     ██████╗  ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    ██████╔╝██║   ██║██████╔╝██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ██║  ██║╚██████╔╝██████╔╝██████╔╝███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
""",end=" ")
    print(color.LIGHTBLACK_EX+"""                                                                                    
 =============================================================================
 #                            Developer:ZeroDey                              #
 #                            YouTube:TheZeroDey                             #
 #                            Contact:t.me/ZeroDey                           #
 #                            Version:1.0                                    #
 =============================================================================
    
     """)

def main_menu():
    sleep(0.1)
    print(color.RED+"[1] " +color.LIGHTYELLOW_EX+"Information Gathering")
    print(color.CYAN+"     ***********************")
    sleep(0.1)
    print(color.RED+"[2] " +color.LIGHTYELLOW_EX+"Cms Robber")
    print(color.CYAN+"     ***********************")
    sleep(0.1)
    print(color.RED+"[3] " +color.LIGHTYELLOW_EX+"About Me")
    print(color.CYAN+"     ***********************")    
    sleep(0.1)
    print(color.RED+"[4] " +color.LIGHTYELLOW_EX+"Exit")
    print(color.CYAN+"     ***********************")    


def info_gathering():
    sleep(0.2)
    print(color.RED+"[1] " +color.LIGHTYELLOW_EX+"IP location Finder")
    print(color.CYAN+"     ***********************")
    
    sleep(0.1)
    print(color.RED+"[2] " +color.LIGHTYELLOW_EX+"WHOIS")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[3] " +color.LIGHTYELLOW_EX+"Admin-finder")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[4] " +color.LIGHTYELLOW_EX+"Port-Scaner")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[5] " +color.LIGHTYELLOW_EX+"DNS-Lookup")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[6] " +color.LIGHTYELLOW_EX+"Robots-Scaner")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[7] " +color.LIGHTYELLOW_EX+"‌Bypass-CloudFlare")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[8] " +color.LIGHTYELLOW_EX+"Cms-Detect")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[9] " +color.LIGHTYELLOW_EX+"back to menu")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[10] " +color.LIGHTYELLOW_EX+"Exit")
    print(color.CYAN+"     ***********************")


def cms_robber():
    sleep(0.2)
    print(color.RED+"[1] " +color.LIGHTYELLOW_EX+"Word-Press")
    print(color.CYAN+"     ***********************")


def infowp():

    sleep(0.2)
    print(color.RED+"[1] " +color.LIGHTYELLOW_EX+"Get-Plugins")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[2] " +color.LIGHTYELLOW_EX+"Find-Usernames")
    print(color.CYAN+"     ***********************")

    sleep(0.1)
    print(color.RED+"[3] " +color.LIGHTYELLOW_EX+"back to menu")
    print(color.CYAN+"     ***********************")



def pdeveloper():
    sleep(0.2)
    print(color.LIGHTBLACK_EX+"\t...:: Developer ==> @ZeroDey ::...")

    sleep(0.1)
    print(color.LIGHTCYAN_EX+"...:: Telegram Channel ==> @Zeroo_Dey ::...")

    sleep(0.1)
    print(color.LIGHTYELLOW_EX+"\t...:: Instagram ==> Zero_Dey ::...")

    sleep(0.1)
    print(color.RED+"...:: YouTube ==> TheZeroDey ::...")

    sleep(0.1)
    print(color.GREEN+"\t-_- Thanks For Using This Tool -_- ")

    try:
        input(color.LIGHTRED_EX+" \n[*]  Back To Menu (Press Enter...) ")
    
    except:
        print(color.RED+"Something bad happend....")
        sys.exit()
