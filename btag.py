import requests
import urllib3
import time
from bs4 import BeautifulSoup

urllib3.disable_warnings()
hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
BV = 'BV1xP411U79V'
def get_tag(BV):
    url = f"https://www.bilibili.com/video/{BV}/"
    r = requests.get(url, headers=hd, verify=False)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,'lxml')
    alltag =soup.find_all('a',attrs={'class':'tag-link'})
    tags = [tag.string.replace(' ','').replace('\n','') for tag in alltag if tag.string != None]
    return tags