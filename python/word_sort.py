
N=int(input())
wrd=[]
for _ in range(N):
    tmp=input()
    wrd.append(tmp)

wrd_s=set(wrd)
wrd_n=list(wrd_s)

cnt=1
while cnt<51:
    tmp_wrd = []
    for i in wrd_n:
        if len(i)==cnt:
            tmp_wrd.append(i)
    tmp_wrd.sort()
    for j in tmp_wrd:
        print(j)
    cnt=cnt+1