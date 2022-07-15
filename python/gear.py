from collections import deque

gears=[]
for _ in range(4):
    gear=input()
    gear=list(gear)
    gears.append(gear)
gears=deque(gears)


K=int(input())
for _ in range(K):
    rotation=[0,0,0,0]
    n, m=map(int, input().split())
    rotation[n-1]=m
    N=n-1
    while N-1 >= 0:
        if gears[N][6]==gears[N-1][2]:
            break
        else:
            if rotation[N]==1:
                rotation[N-1]=-1
                N=N-1
            else:
                rotation[N-1]=1
                N=N-1

    M=n-1
    while M+1 <= 3:
        if gears[M][2]==gears[M+1][6]:
            break
        else:
            # 괄호 =과 == 조심!!
            if rotation[M]==1:
                rotation[M+1]=-1
                M=M+1
            else:
                rotation[M+1]=1
                M=M+1

    # rotation 통해서 틀린 부분 점검!
    for i in rotation:
        tmp=gears[0]
        gears.popleft()
        tmp=deque(tmp)
        tmp.rotate(i)
        gears.append(tmp)

ans=0
if gears[0][0]=='1':
    ans=ans+1
if gears[1][0]=='1':
    ans=ans+2
if gears[2][0]=='1':
    ans=ans+4
if gears[3][0]=='1':
    ans=ans+8
print(ans)
