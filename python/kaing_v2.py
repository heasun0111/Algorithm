#카잉 달력
T=int(input())
for _ in range(T):
    M, N, x, y = map(int,input().split())
    flag=False
    while x<=M*N:
        if x%N==y%N:
            print(x)
            flag=True
            break
        x=x+M

    if flag==False:
        print(-1)
