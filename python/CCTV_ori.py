# 사각지대 개수 카운팅
# CCTV 모든 경우의 수 #으로 출력
# CCTV
from itertools import product

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

x=[1,0,-1,0]
y=[0,1,0,-1]

def CCTV1(room, dx, dy, num):
    nx=dx
    ny=dy
    while 0<=nx<N-1 and 0<=ny<M-1 and room[ny][nx]!=6:
        nx=nx+x[num]
        ny=ny+y[num]
        if room[ny][nx]==0:
            room[ny][nx]=9
        elif room[ny][nx]==6:
            break
        else:
            continue

    return room

def CCTV2(room, dx, dy, num):
    for dir in [0,2]:
        nx = dx
        ny = dy
        dir=dir+num
        while 0 <= nx < N-1 and 0 <= ny < M-1 and room[ny][nx] != 6:
            nx = nx + x[dir]
            ny = ny + y[dir]
            if room[ny][nx] == 0:
                room[ny][nx] = 9
            elif room[ny][nx] == 6:
                break
            else:
                continue
    return room

def CCTV3(room, dx, dy, num):
    for dir in [0,1]:
        nx = dx
        ny = dy
        dir=dir+num
        if dir>4:
            dir=dir/4
        while 0 <= nx < N-1 and 0 <= ny < M-1 and room[ny][nx] != 6:
            nx = nx + x[dir]
            ny = ny + y[dir]
            if room[ny][nx] == 0:
                room[ny][nx] = 9
            elif room[ny][nx] == 6:
                break
            else:
                continue
    return room

def CCTV4(room, dx, dy, num):
    for dir in [0,1,2]:
        nx=dx
        ny=dy
        dir=dir+num
        if dir>4:
            dir=dir/4
        while 0 <= nx < N-1 and 0 <= ny < M-1 and room[ny][nx] != 6:
            nx = nx + x[dir]
            ny = ny + y[dir]
            if room[ny][nx] == 0:
                room[ny][nx] = 9
            elif room[ny][nx] == 6:
                break
            else:
                continue
    return room

def CCTV5(room, dx, dy):
    for dir in range(4):
        nx = dx
        ny = dy
        while 0 <= nx < N-1 and 0 <= ny < M-1 and room[ny][nx] != 6:
            nx = nx + x[dir]
            ny = ny + y[dir]
            if room[ny][nx] == 0:
                room[ny][nx] = 9
            elif room[ny][nx] == 6:
                break
            else:
                continue
    return room


def counting(room):
    count=0
    for i in range(N):
        for j in range(M):
            if room[i][j]==0:
                count=count+1

    return count

CCTV_Point=[]
CCTV_Point2=[]
for n in range(N):
    for m in range(M):
        if room[n][m]==5:
            CCTV5(room, m, n)

        elif room[n][m]==1:
            #CCTV_Point.append([1,m,n])
            CCTV1(room, m, n, 0)
        elif room[n][m]==3:
            CCTV_Point.append([3,m,n])
        elif room[n][m]==4:
            CCTV_Point.append([4,m,n])
        elif room[n][m]==2:
            CCTV_Point2.append([m,n])

# 중복 순열 이용해서 모든 경우의 수 탐색...?

# 라이브러리 쓰지않고 DFS 이용해서 중복조합 구현!!
for tmp in product(range(4)):
    print(tmp)

    
'''
l=[4,4,2,2]
n=len(l)
answer=[]

def dfs(idx, list):
    if len(list)==n:
        answer.append((list[:]))
        return

    for i in range(idx,n):
        dfs(i+1, list+[l[i]])

dfs(0, [])

print(answer)
'''
