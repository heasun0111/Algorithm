#그래프 탐색을 위한 BFS/DFS
from collections import deque

h=10
w=8
field=[]

def DFS(x, y):
    dx=[1,1,-1,-1]
    dy=[1,-1,1,-1]

    field[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny]==1:
            DFS(nx,ny)

def BFS(x, y):
    dx=[1,1,-1,-1]
    dy=[1,-1,1,-1]
    field[x][y]=0
    q=deque()
    q.append([x,y])

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny]==1:
                field[nx][ny]=0
                q.append([nx, ny])
