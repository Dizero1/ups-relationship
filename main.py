from btag import *
import json

tid = 2885698
tname = '小由'

print(f'loading:videolist of \'{tname}\' tag(40 in 1 page)')
blist = []
n = 5
for i in range(1,n+1):
    blist = blist + bvidlist_bytid(tid,i)
blist = list(set(blist))   
print(f'loading:video of the list')

input('continue:')
vlist = [Video(bvid) for bvid in blist]
print('loading completed')

data = pd.DataFrame([v.stat for v in vlist])
data.to_json(f'./data_test/{tid}_{int(time.time())}.json','records',force_ascii=False)

num = 1
num = int(input('which video:'))
while num > 0:
    key = input('which key:')
    if key == 'all':
        print(vlist[num-1].stat)
    else:
        try:
            print(vlist[num-1].stat[key])
        except:
            print(key, 'keyerror')
    try:
        num = int(input('which video:'))
    except:
        pass
    else:
        num=0
