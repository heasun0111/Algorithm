import sys

N, M = map(int, input().split())
person = list(map(int, input().split()))

visited = []
# 한 줄로 요약
for i in range(N):
    visited.append(0)

for j in range(M):
    A, B = map(int, input().split())
    if A > B:
        visited[B - 1] = 1
    elif A < B:
        visited[A - 1] = 1
    else:
        visited[A - 1] = 1
        visited[B - 1] = 1

ans = 0
for k in range(N):
    if visited[k] == 0:
        ans = ans + 1
print(ans)