import requests
import urllib3
import time
import re
import copy
from bs4 import BeautifulSoup

urllib3.disable_warnings()
hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

class Video:
    def __init__(self,bvid:str) -> None:
        self.stat = {
        'code': 1,#0：成功 -400：请求错误 -403：权限不足 -404：无视频 62002：稿件不可见 62004：稿件审核中
        'title': '视频不存在或不可见',
        'up_uid': 0,
        'up_name':'无',
        'pubdate':0,
        'aid': 0,
        'bvid': 'BV',
        'view': 0,
        'danmaku': 0,
        'reply': 0,
        'favorite': 0,
        'coin': 0,
        'like': 0,
        'tag':[
            ]    
        }
        self.stat.update(self.statget(bvid))
    def __str__(self) -> str:
        return self.stat['title']
    def statget(self,bvid:str):
        url = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={bvid}"
        r = requests.get(url, headers=hd, verify=False)
        r.raise_for_status()
        stat = copy.deepcopy(self.stat)
        try:
            stat['code'] = r.json()['code']
            stat['up_uid'] = r.json()['data']['Card']['card']['mid']
            stat['up_name'] = r.json()['data']['Card']['card']['name']
        except KeyError:
            pass
        for k,v in stat.items():
            for data in [r.json()['data']['View'],r.json()['data']['View']['stat']]:
                try:
                    stat[k] = data[k]
                except KeyError:
                    pass
                else:
                    break
        stat['tag'] = [{'tag_id':data['tag_id'],'tag_name': data['tag_name']} for data in r.json()['data']['Tags']]
        time.sleep(0.02)            
        return stat
        
    
bvid = 'BV1xP411U79V'#for test

def get_tagid(bvid):
    url = f"https://api.bilibili.com/x/tag/archive/tags?bvid={bvid}"
    r = requests.get(url, headers=hd, verify=False)
    r.raise_for_status()
    return [data['tag_id'] for data in r.json()['data']]

def bvidlist_bytid(tid:int, pn=1):
    url = f"https://api.bilibili.com/x/tag/detail?pn={pn}&ps=40&tag_id={tid}"
    rt = requests.get(url, headers=hd, verify=False)
    return [ar['bvid'] for ar in rt.json()['data']['news']['archives']]