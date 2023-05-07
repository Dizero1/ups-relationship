import requests
import urllib3
import time
import re
import copy
import pandas as pd

urllib3.disable_warnings()
hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

v_in={}
def singleton(cls):
    def inner(bvid, stat=None):
        if bvid not in v_in.keys():
            v_in[bvid] = cls(bvid,stat)
        return v_in[bvid]
    return inner

@singleton
class Video:
    def __init__(self, bvid:str, stat=None):
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
        if stat == None:
            self.stat.update(self.statget(bvid))
        else:
            self.stat.update(stat)

    def __repr__(self) -> str:
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
        

# def get_tagid(bvid):
#     url = f"https://api.bilibili.com/x/tag/archive/tags?bvid={bvid}"
#     r = requests.get(url, headers=hd, verify=False)
#     r.raise_for_status()
#     return [data['tag_id'] for data in r.json()['data']]

def bvidlist_bytid(tid:int, pn=1):
    url = f"https://api.bilibili.com/x/tag/detail?pn={pn}&ps=40&tag_id={tid}"
    rt = requests.get(url, headers=hd, verify=False)
    return [ar['bvid'] for ar in rt.json()['data']['news']['archives']]

def readblist(tid,n=5):
    blist = set()
    for i in range(1,n+1):
        blist = blist | set(bvidlist_bytid(tid,i))
        time.sleep(0.05)
    return list(blist)

def totagid(tag_name):
    url = f"https://api.bilibili.com/x/tag/info?tag_name={tag_name}"
    r = requests.get(url, headers=hd, verify=False)
    return r.json()['data']['tag_id']

def totagname(tag_id):
    url = f"https://api.bilibili.com/x/tag/info?tag_id={tag_id}"
    r = requests.get(url, headers=hd, verify=False)
    return r.json()['data']['tag_name']

def tagcon(bvid,a:list,b:list):
    bB = False
    aB = False
    for t in Video(bvid).stat['tag']:
        for at in a:
            aB = aB or at == t['tag_id']
        for bt in b:
            bB = bB or bt == t['tag_id']
    return aB and bB
    