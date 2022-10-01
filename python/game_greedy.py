
N=int(input())
score=[]

for _ in range(N):
    S=int(input())
    score.append(S)

ans=0

for i in range(N-1,0,-1):
    if score[i]<=score[i-1]:
        #빼는 순서
        ans=ans+(score[i-1]-score[i]+1)
        score[i-1]=score[i]-1
    else:
        continue

print(ans)
