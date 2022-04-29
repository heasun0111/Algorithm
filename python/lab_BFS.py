# 3칸 넣는거, BFS, 안전영역 탐색
import copy
from collections import deque
from itertools import combinations


N, M = map(int,input().split())
lab=[list(map(int, input().split())) for _ in range(N)]
labTmp=copy.deepcopy(lab)
q=deque()
answer = 0

zeroPoint=[]
for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            zeroPoint.append([i,j])

def findZero(labTmp):
    cnt=0
    for i in range(N):
        for j in range(M):
            if labTmp[i][j]==0:
                cnt=cnt+1
    return cnt

# x,y 좌표 헷갈리지 않고 넣기
def makeQ(labTmp):
    for i in range(N):
        for j in range(M):
            if labTmp[i][j]==2:
                q.append([j,i])
    return q


def BFS(labTmp,q):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<M and 0<=ny<N and labTmp[ny][nx]==0:
                q.append([nx,ny])
                labTmp[ny][nx]=2


#combinations은 튜플 형식!!
def buildWall():
    global answer
    for WallCobi in combinations(zeroPoint, 3):
        labTmp = copy.deepcopy(lab)
        global q
        q.clear()
        for k in WallCobi:
            y=k[0]
            x=k[1]
            labTmp[y][x]=1
        #위에 선언한 함수 실행
        q=makeQ(labTmp)
        BFS(labTmp,q)
        tmp=findZero(labTmp)
        if tmp>answer:
            answer=tmp

buildWall()
print(answer)


