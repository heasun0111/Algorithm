# 장애물 고려하지 않고 거리를 구함 -> visited 이용!!
from collections import deque

q=deque()

N=int(input())
sea=[list(map(int, input().split())) for _ in range(N)]
shark_w=2
eat_fish=0

# x,y 좌표 헷갈리지 않기!
# 물고기 좌표 찾기
def findFish(shark_w, sea):
    fish = []
    for j in range(N):
        for i in range(N):
            if sea[j][i]<shark_w and sea[j][i]!=0:
                fish.append([j,i])

    if len(fish)==0:
        return 0
    else:
        return fish


# 상어&물고기 좌표를 주면 최소 이동 경로 구하는 거
def bfs(shk_x, shk_y, fishSpot, shark_w):
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

    min=40001
    min_x=-1
    min_y=-1
    # fishSpot에 있는 x,y좌표 헷갈렸었음!
    for tmp in fishSpot:
        #예외 생각! 방문할 수 없는 물고기 카운팅x
        if visited[tmp[0]][tmp[1]]!=0 and min>visited[tmp[0]][tmp[1]]:
            min=visited[tmp[0]][tmp[1]]
            min_x=tmp[1]
            min_y=tmp[0]
    sea[min_y][min_x]=0
    shk_x=min_x
    shk_y=min_y
    return [min, shk_x, shk_y]

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
    fishSpot=findFish(shark_w, sea)
    cnt=0
    flag=True
    if fishSpot==0:
        flag=False

    while flag==True:
        result=bfs(shk_x, shk_y, fishSpot, shark_w)
        if result[0]==40001:
            flag=False
            break

        cnt=cnt+result[0]
        # 상어 좌표 다시 조정
        shk_x, shk_y = result[1], result[2]
        eat_fish=eat_fish+1
        # 물고기 먹는거 중복 됐었음
        if eat_fish >= shark_w:
            shark_w=shark_w+1
            eat_fish=0
        fishSpot = findFish(shark_w,sea)

        if fishSpot==0:
            flag=False
            break

    return cnt

print(calTime(sea))


# 내가 실수했던 부분
# 상어 위치 0으로 바꾸기
# 갈 수 없는 물고기(visited==0) 먹지 않기
# 아무것도 못 먹는 경우 무한 루프 -> 시간 초과
# 좌표 x,y 순서 헷갈리지 말기
# 물고기 먹는거 코드 중복
