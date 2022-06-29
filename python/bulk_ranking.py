
N=int(input())
bulk=[]

for _ in range(N):
    w,h = map(int, input().split())
    bulk.append([w,h])

ans=[]
for i in range(N):
    ranking=1
    for j in range(N):
        if i==j:
            continue

        else:
            if bulk[i][0]<bulk[j][0] and bulk[i][1]<bulk[j][1]:
                ranking=ranking+1

    ans.append(str(ranking))

answer=" ".join(ans)
print(answer)
