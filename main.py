from btag import *

tid = 2885698
tname = '小由'
print(f'loading:list of {tname} (40 for 1 page)')
vlist = [video(bvid) for bvid in bvidlist_bytid(tid)]
print('losding completed')
num = 1
while num != 0:
    num = int(input('which video:'))
    key = input('which key:')
    if key == 'all':
        print(vlist[num-1].stat)
    else:
        try:
            print(vlist[num-1].stat['title'])
        except:
            print(key, 'keyerror')