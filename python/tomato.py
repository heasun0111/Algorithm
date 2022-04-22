from collections import deque

M, N = map(int,input().split())
box=[list(map(int, input().split())) for _ in range(N)]

def BFS(x, y):
    cnt=0
    dx=[1,1,-1,-1]
    dy=[1,-1,1,-1]
    que=deque()
    que.append([x,y])
    while len(que)!=0:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N and box[nx][ny]==0:
                box[nx][ny]=1
                que.append([nx, ny])
            cnt=cnt+1

    return cnt

for i in range(M):
    for j in range(N):
        if box[j][i]==1:
            print(BFS(i,j))