
T=int(input())
for tc in range(T):
    N=int(input())
    price=list(map(int, input().split()))

    max_P=-1
    selling=[0 for _ in range(N)]

    for i in range(N):
        if price[N-i-1]>max_P:
            max_P=price[N-i-1]

        else:
            selling[N-i-1]=max_P-price[N-i-1]

    ans=sum(selling)
    print('#'+str(tc+1)+' '+str(ans))

