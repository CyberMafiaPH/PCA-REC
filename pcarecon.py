#Philippine CyberAlliance Recon Tools
#Coded by Vend3ttA
import os
from time import sleep
import requests

def clearScreen():
    os.system("cls" if os.name == 'nt' else "clear")

def starter():
    clearScreen()
    print("""
\033[35m╔═╗╔═╗╔═╗   ╦═╗╔═╗╔═╗╔═╗╔╗╔\033[36m
\033[37m╠═╝║  ╠═╣───╠╦╝║╣ ║  ║ ║║║║\033[31m
\033[33m╩  ╚═╝╩ ╩   ╩╚═╚═╝╚═╝╚═╝╝╚╝\033[37m
\033[33mWeb\033[37m Reconnaisance\033[34m Tools\033[0m
""")
    
def pca_menu():
    starter()
    print("""
Please choose
1.DNS Lookup
2.Reverse DNS
3.Track IP Address
4.Reverse IP Lookup
5.HTTP headers check
6.Extract Pagelinks
7.AS Lookup
8.Whois Server Lookup
""")
    while 1:  
            choose = input("\033[36mPCA@PANEL:~$\033[0m ")
            if choose in ["exit", "e", "EXIT"]:
                print("[*] Exiting...")
                sleep(2)
                exit("\033[31m[*] Done exiting\033[0m")
            elif choose in ["1"]:
                clearScreen()
                starter()

                target_url = input("\033[36mTarget: \033[0m")
                print("\033[31mExtracting DNS....\033[0m")
                sleep(2)

                result = requests.get("https://api.hackertarget.com/dnslookup/?q={}".format(target_url)).text
                print("\033[31m[*] Done\033[0m")
                print(result)
                back_to_menu()
            elif choose in ["2"]:
                clearScreen()
                starter()

                target_url = input("\033[36mTarget: \033[0m")
                print("\033[31mExtracting Reverse DNS Records....\033[0m")
                sleep(2)

                result = requests.get("https://api.hackertarget.com/reversedns/?q={}".format(target_url)).text
                print("\033[31m[*] Done\033[0m")
                print(result)
                back_to_menu()
            elif choose in ["3"]:
                clearScreen()
                starter()

                target_url = input("\033[36mEnter Target IP: \033[0m")
                print("\033[31mTracking estimated geolocation....\033[0m")
                sleep(2)

                os.system(f"curl https://ipapi.co/{target_url}/json")
                print("\033[31m\n[*] Done\033[0m")
                back_to_menu()
            elif choose in ["4"]:
                clearScreen()
                starter()

                target_url = input("\033[36mTarget: \033[0m")
                print("\033[31mExtracting Sites....\033[0m")
                sleep(2)

                result = requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(target_url)).text
                print("\033[31m[*] Done\033[0m")
                print(result)
                back_to_menu()
            elif choose in ["5"]:
                clearScreen()
                starter()

                target_url = input("\033[36mTarget: \033[0m")
                print("\033[31mExtracting HTTP headers....\033[0m")
                sleep(2)

                result = requests.get("https://api.hackertarget.com/httpheaders/?q={}".format(target_url)).text
                print("\033[31m[*] Done\033[0m")
                print(result)
                back_to_menu()
            elif choose in ["6"]:
                clearScreen()
                starter()

                target_url = input("\033[36mTarget: \033[0m")
                print("\033[31mExtracting Reverse DNS Records....\033[0m")
                sleep(2)

                result = requests.get("https://api.hackertarget.com/pagelinks/?q={}".format(target_url)).text
                print("\033[31m[*] Done\033[0m")
                print(result)
                back_to_menu()
            elif choose in ["7"]:
                clearScreen()
                starter()

                target_url = input("\033[36mTarget: \033[0m")
                print("\033[31mExtracting Reverse DNS Records....\033[0m")
                sleep(2)

                result = requests.get("https://api.hackertarget.com/aslookup/?q={}".format(target_url)).text
                print("\033[31m[*] Done\033[0m")
                print(result)
                back_to_menu()
            elif choose in ["8"]:
                clearScreen()
                starter()

                target_url = input("\033[36mEnter Target IP: \033[0m")
                print("\033[31mTracking estimated geolocation....\033[0m")
                sleep(2)

                os.system(f"whois {target_url}")
                print("\033[31m\n[*] Done\033[0m")
                back_to_menu()

def back_to_menu():
    menu = input("[PCA-AI]:~$Do you want to go back to menu?(y/n) ")
    if menu in ["y","Y","Yes","YES"]:
        pca_menu()
    elif menu in ["exit","e"]:
        print("[*] Exiting...")
        sleep(2)
        exit("\033[31m[*] Done exiting\033[0m")
    elif menu in ["no","n"]:
        exit()
    else:
        print("[*] Invalid Command! ")
pca_menu()
