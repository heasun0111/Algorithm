
N, K = map(int,input().split())
cost=list(map(int, input().split()))
ans=0

idx=0
while idx<N:
    tmp = 100000000001
    if idx+K>N:
        break
    else:
        for i in range(K):
            if cost[idx + i] <= tmp:
                tmp_idx = i
                tmp=cost[idx + i]
        if cost[idx + tmp_idx] > ans:
            ans = cost[idx + tmp_idx]
        idx = idx + tmp_idx + 1

print(ans)

