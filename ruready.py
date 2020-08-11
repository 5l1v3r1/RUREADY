#coding-utf8

import random
import pyfiglet
import time
import os
import string
import urllib
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

ascii_banner = pyfiglet.figlet_format("R U READY ?")
print(ascii_banner)
print("RUREADY - A TOOL BY UAYEB5")
print("This tool is for educational purpose only !\n")
print(" ")

time.sleep(2.0)

print(Fore.GREEN + "[+] What do you want to do ?\n")
print(Style.RESET_ALL)
b = input("[+] Find a victim for SQL Injection 1 ? for XSS Cross Site Scripting 2 ?\n> ")
print(Style.RESET_ALL)

try:
	b = str(b)
except:
	print(Fore.RED + "Incorrect value.")
	print(Style.RESET_ALL)

if b == '1':

    def sql(): 

    	USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    	MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    
    	fin = open('sqdo.txt')

    	for line in fin:
    
        	query = line
        	query = query.replace(' ', '+')
        	URL = f"https://google.com/search?q={query}"

        	headers = {"user-agent": USER_AGENT}
        	resp = requests.get(URL, headers=headers)

        	if resp.status_code == 200:
            		soup = BeautifulSoup(resp.content, "html.parser")
            		results = []
            		for g in soup.find_all('div', class_='r'):
                		anchors = g.find_all('a')
                		if anchors:
                    			link = anchors[0]['href']
                    			title = g.find('h3').text
                    			item = {
                        			"link": link
                    			}
                    			results.append(item)
            		print(*results, sep = '\n')
            		print(Fore.GREEN + '[+] Total vulnerable websites found : %s ' % str( len( results ) ) ) 
            		print(" ")            
            		print(Style.RESET_ALL)
            		print(Fore.RED + "[+] !!! WARNING !!!\n")
            		print(Fore.RED + "[+] Never attack a website you don't have permission for.\n")
            		print(Style.RESET_ALL)
            		time.sleep(2.0)

            		print(Fore.GREEN + "[+] LOADING OTHER WEBSITES...\n")
            		print(Style.RESET_ALL)
            		time.sleep(3.0)
    sql()
   
elif b == '2':

    def xss():
    	print(" ")

    	USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    	MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

    	fin = open('xdo.txt')

    	for line in fin:

        	query = line
        	query = query.replace(' ', '+')
        	URL = f"https://google.com/search?q={query}"

        	headers = {"user-agent": USER_AGENT}
        	resp = requests.get(URL, headers=headers)

        	if resp.status_code == 200:
            		soup = BeautifulSoup(resp.content, "html.parser")
            		results = []
            		for g in soup.find_all('div', class_='r'):
                		anchors = g.find_all('a')
                		if anchors:
                    			link = anchors[0]['href']
                    			title = g.find('h3').text
                    			item = {
                        		"link": link
                    			}
                    			results.append(item)
            		print(*results, sep = '\n')
            		print(Fore.GREEN + '[+] Total vulnerable websites found : %s ' % str( len( results ) ) ) 
            		print(" ")
            		print(Style.RESET_ALL)
            		print(Fore.RED + "[+] !!! WARNING !!!\n")
            		print(Fore.RED + "[+] Never attack a website you don't have permission for.\n")
            		print(Style.RESET_ALL)
            		time.sleep(2.0)

            		print(Fore.GREEN + "[+] LOADING OTHER WEBSITES...\n")
            		print(Style.RESET_ALL)
            		time.sleep(3.0)
    xss()
    
else:
    print(" ")
    print("Are you high ? Bye.")
    raise SystemExit
              
