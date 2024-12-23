# writen by m.e.
# version 1.0



############################################################
#                         IMPORT                           #
############################################################

import os
import time
from colorama import Fore, Style
from subprocess import Popen, call, PIPE
import socket, socketserver
import http
import glob


def html_copy_and_run_on_local_wifi():

    def delete_files():
        for file in glob.glob("index.html"):
            os.remove(file)
############################################################
#                      RUN SCRIPT ON WIFI                 #
############################################################

    def run_scritp_on_local_wifi():

        # Grabs IP
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        # Asks on port
        PORT = input(int("[" + Fore.RED + ">" + Style.RESET_ALL + "] Enter port number for creating server: "))

        # Html path
        directory = os.path.dirname(os.path.realpath(__file__))
        os.chdir(directory)


        class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.path = 'index.html' # Name of the file
                return http.server.SimpleHTTPRequestHandler.do_GET(self)

        # Creates server on IP and port
        with socketserver.TCPServer((ip_address, PORT), MyHttpRequestHandler) as httpd:
            print(f"[" + Fore.RED + ">" + Style.RESET_ALL + "] Serving on {ip_address}:{PORT}")
            httpd.serve_forever()
    

############################################################
#                      COPY WIFI HTML CODE                 #
############################################################
    def copy_web_site():
        delete_files()


        directory = os.path.dirname(os.path.realpath(__file__))  # Získání cesty k adresáři skriptu
        os.chdir(directory)

        # Info about web and folder
        folder = os.getcwd()
        web_name = input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Please input web name: (https://www.example.com) ")



        # Copies html code into current folder
        print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Wait please, this will take a while")
        Popen(['sudo', 'httrack', web_name, '-O', folder])
    

    copy_web_site()
    run_scritp_on_local_wifi()







