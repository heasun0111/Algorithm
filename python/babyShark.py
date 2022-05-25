# 거리 및 조건을 파악해서 먹을 물고기 탐색 -> 없으면 끝낸다
# 상어부터 물고기까지 거리를 구하는 부분
# 상어가 먹은 물고기 개수
from collections import deque

q=deque()

N=int(input())
sea=[list(map(int, input().split())) for _ in range(N)]
shark_w=2
eat_fish=0

# x,y 좌표 헷갈리지 않기!
# 물고기 좌표 찾기
def findFish(shark_w, sea, shk_x, shk_y):
    fish = []
    for i in range(N):
        for j in range(N):
            if sea[j][i]<shark_w and sea[j][i]!=0:
                fish.append([j,i])

    if len(fish)==0:
        return 0
    else:
        min = 40001
        min_x=-1
        min_y=-1
        fish.sort(key=lambda x:(x[0], x[1]))
        for tmp in fish:
            dis=abs(shk_y-tmp[0])+abs(shk_x-tmp[1])
            if dis<min:
                min=dis
                min_x=tmp[1]
                min_y=tmp[0]
        return [min_x, min_y]


# 상어&물고기 좌표를 주면 최소 이동 경로 구하는 거
def bfs(shk_x, shk_y, fish_x, fish_y, shark_w):
    visited=[[0 for _ in range(N)]for _ in range(N)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    q.append([shk_x, shk_y])
    while q:
        c, d=q.popleft()
        for i in range(4):
            nx=c+dx[i]
            ny=d+dy[i]
            if 0<=nx<N and 0<=ny<N and sea[ny][nx]<=shark_w and visited[ny][nx]==0:
                visited[ny][nx]=visited[d][c]+1
                q.append([nx,ny])
    return visited[fish_y][fish_x]

def calTime(sea):
    for n in range(N):
        for m in range(N):
            if sea[m][n]==9:
                shk_x, shk_y = n, m
                sea[m][n] = 0
                break
    global shark_w
    global eat_fish
    #여기서 좌표 실수
    fishSpot=findFish(shark_w, sea, shk_x, shk_y)
    cnt=0
    while fishSpot!=0:
        u,v=fishSpot[0],fishSpot[1]
        cnt=cnt+bfs(shk_x, shk_y,u,v,shark_w)
        eat_fish=eat_fish+1
        sea[v][u]=0
        # 상어 좌표 다시 조정
        shk_x, shk_y = fishSpot[0], fishSpot[1]
        # 물고기 먹는거 중복 됐었음
        if eat_fish >= shark_w:
            shark_w=shark_w+1
            eat_fish=0
        fishSpot = findFish(shark_w,sea, shk_x, shk_y)

    return cnt

print(calTime(sea))