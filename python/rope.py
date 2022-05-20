N=int(input())
rope=[]
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

answer=rope[0]
sum=0

for i in range(N):
    sum=sum+rope[i]
    if sum/(i+1)>=answer:
        answer=sum/(i+1)
    else:
        break

print(int(answer))
