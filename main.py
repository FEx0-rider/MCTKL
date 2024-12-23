# writen by m.e.
# version 1.0


end = """ 
If you found error pleare report it to m.e.

Thank you for using MCTKL!
"""

from load_page import load_page_welcome
import time
from colorama import Fore, Style

try:
    if __name__ == "__main__":
        
        welcome_num = load_page_welcome() # Welcome num is first input
    

    ############################################################
    #                             WIFI                         #
    ############################################################
        if welcome_num == 1:
            from load_page import load_page_wifi

            wifi_load_page_num = load_page_wifi() # Load page for wifi
            time.sleep(1)

            if wifi_load_page_num == 1:
                from wifi_client_deauth import wifi_client_deauth # Load def for client deauthorization 
                wifi_client_deauth()    # Runs client deauthorization

############################################################
#                                WEB                       #
############################################################
        if welcome_num == 2:
            from load_page import load_page_web

            web_load_page_num = load_page_web() # Load page for web
            time.sleep(1)

            if web_load_page_num == 1 :
                from html_copy_and_run_on_local_wifi import html_copy_and_run_on_local_wifi # Load def for web copy...
                html_copy_and_run_on_local_wifi() # Runs web copy...


except KeyboardInterrupt:
    
    print('\n' + '\n')
    print(Fore.RED + end + Style.RESET_ALL)
    print('\n' + '\n')