
N, M = map(int, input().split())
S=[]
S_M=[]

for _ in range(N):
    tmp=input()
    S.append(tmp)

for _ in range(M):
    tmp2=input()
    S_M.append(tmp2)

ans=0
for str_M in S_M:
    if str_M in S:
        ans=ans+1
    else:
        continue

print(ans)