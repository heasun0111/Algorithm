#카잉 달력
import math

def lcm(a,b):
    return (a*b)//math.gcd(a,b)

T=int(input())
for _ in range(T):
    M, N, x, y = map(int,input().split())
    if M<N:
        #cnt=0
        tmpX=0
        tmpY=0
        flag=False
        #M<N이라서 가능
        tmpX=x
        tmpY=x
        cnt=x
        #최소 공배수
        LCM=lcm(M, N)
        while cnt<=LCM:
            if ((tmpY+M)%N)+1==y:
                flag=True
                cnt+=M
                break
            else:
                tmpY=((tmpY+M)%N)+1
                cnt+=M

    else:
        #cnt=0
        tmpX=0
        tmpY=0
        flag=False
        #M>=N이라서 가능
        tmpX=y
        tmpY=y
        cnt=y
        #최소 공배수
        LCM=lcm(M, N)
        while cnt<=LCM:
            if ((tmpX+N)%M)+1==x:
                flag=True
                cnt+=N
                break
            else:
                tmpX=((tmpX+N)%M)+1
                cnt+=N

    if flag==True:
        print(cnt)
    else:
        print(-1)


#좀 더 변수 줄여서 하기
#tmp,cnt
#같은 기능하는 거 없애기
