import requests
import os
import sys
import time
os.system("clear")
time.sleep(1)
print("""
        \033[1;32m               
RRRRRRRRRRRRRRRRR      SSSSSSSSSSSSSSS 
R::::::::::::::::R   SS:::::::::::::::S
R::::::RRRRRR:::::R S:::::SSSSSS::::::S
RR:::::R     R:::::RS:::::S     SSSSSSS
  R::::R     R:::::RS:::::S            
  R::::R     R:::::RS:::::S            
  R::::RRRRRR:::::R  S::::SSSS         
  R:::::::::::::RR    SS::::::SSSSS    
  R::::RRRRRR:::::R     SSS::::::::SS  
  R::::R     R:::::R       SSSSSS::::S 
  R::::R     R:::::R            S:::::S
  R::::R     R:::::R            S:::::S
RR:::::R     R:::::RSSSSSSS     S:::::S
R::::::R     R:::::RS::::::SSSSSS:::::S
R::::::R     R:::::RS:::::::::::::::SS 
RRRRRRRR     RRRRRRR SSSSSSSSSSSSSSS   
 
""")

m="|——————————————————————————————————————|\n|\033[1;36m  C   R   E   A   T   I   O   N   S\033[1;32m   |\n|——————————————————————————————————————|\033[0m"
for c in m:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.01)
print("\n\n\n\033[41m\033[1;32m||==============================================||\n||      Tools Name  : IP tracking               ||\n||      Designed by : RS Creations              ||\n||	Github      : https://github.com/me-rs  ||\n||==============================================||\033[0m")
time.sleep(2)
print("\n\n")
a="Welcome to \033[1;32mRS Creations"
for c in a:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.2)
time.sleep(2)
n=input("\n\033[1;35mYour name: \033[1;34m")
a="\033[33mHello  \033[1;34m "+n+"\033[33m,\nThis \033[1;32m 'IP Tracking Tools' \033[33m only shows approximate results based on internet.This might not the exact location of your target .\n"
for c in a:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)


ip=input("\033[36mEnter target IP: ")
req= requests.get("http://ip-api.com/json/"+ip)
txt=req.json()
print(f"\033[1;31mQuery for      : {txt['query']}\n\033[34mStatus\t       : Tracking {txt['status']}\n\033[1;32mCountry Name   : {txt['country']}\n\033[1;35mCountry Code   : {txt['countryCode']}\n\033[1;33mDivision Name  : {txt['regionName']}\n\033[1;35mCity\t       : {txt['city']}\n\033[34mTime Zone      : {txt['timezone']}\n\033[1;32mISP\t       : {txt['isp']}\n\033[31mASN\t       : {txt['as']}\n\033[36mLive Location  : https://www.google.com/maps/search/?api=1&query={txt['lat']},{txt['lon']}\033[0m")
