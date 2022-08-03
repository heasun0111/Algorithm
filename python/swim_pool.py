# DP 공부하기
# min(
# 1D랑 1M는 DP에 담고 나머지(3달, 1년)는 DP랑 비교

T=int(input())
dp=[]
for TC in range(1, T+1):
    D1, M1, M3, Y1 = map(int, input().split())
    schedule=list(map(int, input().split()))

    ans=0
    tmp=0
    for i in range(len(schedule)):
        tmp=min(D1*schedule[i], M1)
        dp.append(tmp)
        if i>=2:
            tmp=min(dp[i]+dp[i-1]+dp[i-2], M3)
            if dp[i]!=tmp:
                dp[i]=tmp
                dp[i-1]=0
                dp[i-2]=0


    if sum(dp)>Y1:
        print('#'+str(TC)+' '+str(Y1))
    else:
        print('#' + str(TC) + ' ' + str(sum(dp)))







