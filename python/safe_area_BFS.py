from collections import deque

N=int(input())
area=[list(map(int, input().split())) for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]
#깊은 복사 말고 T/F 이용해서 메모리를 사용하는게 좋다!

minN=min(map(min,area))
maxN=max(map(max,area))

q=deque()

def BFS(x,y,h):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    visited[x][y]=1
    q.append([x,y])
    while q:
        a,b=q.popleft()
        visited[a][b] = 1
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and area[nx][ny]>h:
                visited[nx][ny]=1
                q.append([nx,ny])


def findSafeArea(h):
    cnt=0
    for n in range(N):
        for m in range(N):
            if area[n][m]>h and visited[n][m]==0:
                BFS(n,m,h)
                cnt=cnt+1
    return cnt


answer=[]
for k in range(0, maxN):
    visited=[[0 for _ in range(N)] for _ in range(N)]
    tmp=findSafeArea(k)
    answer.append(tmp)

print(max(answer))
