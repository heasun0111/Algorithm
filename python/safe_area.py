import copy
import sys
sys.setrecursionlimit(10**5)

N=int(sys.stdin.readline())
area=[list(map(int, input().split())) for _ in range(N)]
areaTmp=copy.deepcopy(area)

minN=min(map(min,area))
maxN=max(map(max,area))


def DFS(x,y,h):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    areaTmp[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and areaTmp[nx][ny]>h:
            areaTmp[nx][ny]=0
            DFS(nx,ny,h)


def findSafeArea(h):
    cnt=0
    for n in range(N):
        for m in range(N):
            if areaTmp[n][m]>h:
                DFS(n,m,h)
                cnt=cnt+1
    return cnt


answer=[]
for k in range(0, maxN):
    areaTmp = copy.deepcopy(area)
    tmp=findSafeArea(k)
    answer.append(tmp)

print(max(answer))