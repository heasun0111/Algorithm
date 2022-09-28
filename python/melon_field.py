
K=int(input())
field=[]
idx_w=0
idx_h=0
max_w=0
max_h=0

for i in range(6):
    dir, length = map(int, input().split())
    field.append([length, dir])
    if dir==1 or dir==2:
        if max_h<length:
            max_h=length
            idx_h=i
    elif dir==3 or dir==4:
        if max_w<length:
            max_w=length
            idx_w=i

min_w=0
min_h=0

#방향도 고려해서!
if idx_w+2>5:
    min_w=field[idx_w+2-5][0]
else:
    min_w = field[idx_w+2][0]

if idx_h+2>5:
    min_h=field[idx_h+2-5][0]
else:
    min_h=field[idx_h+2][0]


ans=((max_w*max_h)-(min_w*min_h))*K
print(ans)

