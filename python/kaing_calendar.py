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

       
#테스트 케이스는 처음과 끝 부분을 놓치지말자!!
#이번꺼는 0주기 때를 생각 못함..
