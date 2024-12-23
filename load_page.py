# writen by m.e.
# version 1.0

import colorama
from colorama import Fore, Back, Style


# main loading screen 
welcome = """
FEx0 represents new software:

███╗░░░███╗░█████╗░████████╗██╗░░██╗██╗░░░░░
████╗░████║██╔══██╗╚══██╔══╝██║░██╔╝██║░░░░░
██╔████╔██║██║░░╚═╝░░░██║░░░█████═╝░██║░░░░░
██║╚██╔╝██║██║░░██╗░░░██║░░░██╔═██╗░██║░░░░░
██║░╚═╝░██║╚█████╔╝░░░██║░░░██║░╚██╗███████╗
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

multifunctional cmd tool for kali linux

version: 1.24

"""


# map navigating user
wifi_welcome = """ 
1, Wifi 
    |_ Wifi client deauth
    |_ Wifi password cracker (x)"""
web_welcome = """
2, Web
    |_Html copy and run on local wifi"""
heshes_welcome = """
3, Hashes
    |_Hashes cracker
    |_Hasher generator
"""

############################################################
#    1 CERVENA 2 ZLUTA 3 MODRA 4 CYAN 5 ZELENA 6 MAGENTA   #
############################################################


############################################################
#           DEFINITION THAT PRINT MAP INTO CMD LINE        #
############################################################

def load_page_welcome():
    print(welcome)
    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] (!INFO) Only for education purposes, illegal thing on your responsibility!" '\n \n')
    print(Style.RESET_ALL + "Please select number:")


############################################################
#                    PRINTING MAP NAVIGATING               #
############################################################

    print(Fore.RED + wifi_welcome + Style.RESET_ALL)
    print(Fore.YELLOW + web_welcome + Style.RESET_ALL)
    print(Fore.BLUE + heshes_welcome + Style.RESET_ALL)


############################################################
#                         MAIN MAP                        #
############################################################
    while True:
        try:
            welcome_num = int(input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Number 1 - 5: "))
            if welcome_num <= 0:
                print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
            elif welcome_num >= 6:
                print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
            else:
                return welcome_num
        except ValueError:
            print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")


############################################################
#                      WIFI SELECTION                     #
############################################################
def load_page_wifi():

    # Print all options
    print('\n')
    print(Fore.RED + "1, Wifi client deauth")
    print(Fore.YELLOW + "2, Wifi password cracker (x)" + Style.RESET_ALL)
    print('\n')


    while True:
        try:
            wifi_load_page_num = int(input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Number 1 - 2: "))
            if wifi_load_page_num <= 0:
                print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
            elif wifi_load_page_num >= 3:
                print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
            else:
                print('\n')
                return wifi_load_page_num
        except ValueError:
            print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
        

############################################################
#                       WEB SELECTION                      #
############################################################

def load_page_web():

    # Print all options
    print('\n')
    print(Fore.RED + "1, Html copy and run on local wifi")
    print('\n')


    while True:
        try:
            web_load_page_num = int(input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Number 1 - 2: "))
            if web_load_page_num <= 0:
                print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
            elif web_load_page_num >= 3:
                print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")
            else:
                print('\n')
                return web_load_page_num
        except ValueError:
            print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Try again dumb!!")