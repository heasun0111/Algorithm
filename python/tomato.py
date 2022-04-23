from collections import deque

M, N = map(int,input().split())
box=[list(map(int, input().split())) for _ in range(N)]
que=deque()
cnt=0

for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            que.append([i,j])

def BFS():
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny]==0:
                box[nx][ny]=box[a][b]+1
                que.append([nx, ny])

BFS()

for i in box:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    cnt=max(cnt, max(i))
print(cnt-1)




# 빠트린 부분
# 익은 토마토를 que에다가 넣기
# dx, dy 숫자 잘못 넣음
# while에는 que만 적어도 OK
# for a, b 이후 if에서도 append 하기!
