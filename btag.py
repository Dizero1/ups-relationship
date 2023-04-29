import requests
import urllib3
import time
import re
# from bs4 import BeautifulSoup

urllib3.disable_warnings()
hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
class video:
    def __init__(self,bvid:str) -> None:
        self.stat = {
        'code': int,#0：成功 -400：请求错误 -403：权限不足 -404：无视频 62002：稿件不可见 62004：稿件审核中
        'title': str,
        'up_uid': int,
        'up_name':str,
        'aid': int,
        'bvid': str,
        'view': int,
        'danmaku': int,
        'reply': int,
        'favorite': int,
        'coin': int,
        'like': int,
        'tag':[
            {
            'tag_id':int,
            'tag_name': str
            }
            ]    
        }
        self.stat.update(self.statget(bvid))
    def statget(self,bvid:str):
        url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        r = requests.get(url, headers=hd, verify=False)
        r.raise_for_status()
        stat = {
        'code': int,
        'title': str,
        'up_uid': int,
        'up_name':str,
        'aid': int,
        'bvid': str,
        'view': int,
        'danmaku': int,
        'reply': int,
        'favorite': int,
        'coin': int,
        'like': int,
        'tag':[
            {
            'tag_id':int,
            'tag_name': str
            }
            ]    
        }
        try:
            stat['code'] = r.json()['code']
            stat['up_uid'] = r.json()['data']['owner']['mid']
            stat['up_name'] = r.json()['data']['owner']['name']
        except KeyError:
            pass
        for k,v in stat.items():
            for data in [r.json()['data'],r.json()['data']['stat']]:
                try:
                    stat[k] = data[k]
                except KeyError:
                    pass
                else:
                    break
        url = f"https://api.bilibili.com/x/tag/archive/tags?bvid={bvid}"
        r = requests.get(url, headers=hd, verify=False)
        r.raise_for_status()
        stat['tag'] = [{'tag_id':data['tag_id'],'tag_name': data['tag_name']} for data in r.json()['data']]            
        return stat
        
    
bvid = 'BV1xP411U79V'#for test
def get_tag_byhtml(bvid):
    url = f"https://www.bilibili.com/video/{bvid}/"
    r = requests.get(url, headers=hd, verify=False)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'lxml')
    alltag = soup.find_all('a', attrs={'class':'tag-link'})
    return [tag.string.replace(' ','').replace('\n','') for tag in alltag if tag.string != None]

def get_tagid(bvid):
    url = f"https://api.bilibili.com/x/tag/archive/tags?bvid={bvid}"
    r = requests.get(url, headers=hd, verify=False)
    r.raise_for_status()
    return [data['tag_id'] for data in r.json()['data']]

xy1 =video('BV1xP411U79V')
print(xy1.stat)