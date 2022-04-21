import math

def lcm(a,b):
    return (a*b)//math.gcd(a,b)

T=int(input())
for _ in range(T):
    M, N, x, y = map(int,input().split())

    flag=False
    cnt=x
    LCM=lcm(M, N)
    while cnt<=LCM:
        #처음부터 답이 나오는 경우도 고려!!
        if cnt%N==y%N:
            flag=True
            break
        else:
            cnt+=M

    if flag==True:
        print(cnt)
    else:
        print(-1)

       
