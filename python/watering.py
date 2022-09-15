# 그리디 물주기 구현 어렵.. -> range(0, N, A)를 이용해서 띄엄띄엄 증가 배열 이용!

N, K, A, B = map(int, input().split())
flowerPot=[K for _ in range(N)]

def potCheck(flowerPot):
    flag=True
    for i in range(N):
        if flowerPot[i]==0:
            flag=False
    return flag

Flag=True
ans=0
# 그리디 물주기 구현 어렵;
while Flag:
    for i in range(0, N, A):
        if Flag==False:
            break
        for j in range(A):
            if i+j>=N and i-j>=0:
                flowerPot[i-j] = flowerPot[i-j]+B
            elif i+j<N:
                flowerPot[i+j] = flowerPot[i+j]+B
            else:
                continue

        for j in range(N):
            flowerPot[j]=flowerPot[j]-1
        ans = ans+1
        Flag=potCheck(flowerPot)

        if Flag==False:
            break

print(ans)

