from btag import *

tid = 2885698
tname = '小由'
print(f'loading:list of {tname} (40 for 1 page)')
vlist = [Video(bvid) for bvid in bvidlist_bytid(tid)]
print('loading completed')
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