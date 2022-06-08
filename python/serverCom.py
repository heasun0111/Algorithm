
N=int(input())

server=[list(map(int, input().split())) for _ in range(N)]

computer=[0 for _ in range(10000000)]
computer_C=[0 for _ in range(10000000)]

for i in range(N):
    for j in range(N):
        if server[j][i]!=0:
            computer[server[j][i]] = computer[server[j][i]] + 1
        else:
            continue

for i in range(10000000-1):
    computer_C[i+1]=computer_C[i]+computer[i+1]


