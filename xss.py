import random
import string
import urllib
import requests
import time
from bs4 import BeautifulSoup

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
        print( '\nTotal vulnerable websites found : %s ' % str( len( results ) ) ) 
        print(" ")
        print("!!! WARNING !!!")
        print(" ")
        print("Always check and analyse your victim before attacking it.")
        print("Never attack a website you don't have permission for.")
        print(" ")
        time.sleep(2.0)

        print("LOADING OTHER WEBSITES...")
