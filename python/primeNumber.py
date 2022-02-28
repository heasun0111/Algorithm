import sys

N=int(input())
primeNumber=list(range(2,N+1))
ans=[]

for i in primeNumber:
    for j in range(len(primeNumber)):
        if primeNumber[j]!=i and primeNumber[j]%i==0 and (primeNumber[j] not in ans):
            ans.append(primeNumber[j])

for k in range(len(ans)):
    num=ans[k]
    primeNumber.remove(num)

print(primeNumber)