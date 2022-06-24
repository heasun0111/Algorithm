# 사각지대 개수 카운팅
# CCTV 모든 경우의 수 #으로 출력
# CCTV

# CCTV 영역 넘어가는 거
# CCTV5 제대로 작동 X
# 모든 경우의 수 탐색 X

from collections import deque
import copy

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

x=[1,0,-1,0]
y=[0,1,0,-1]

def CCTV1(room, dx, dy, num):
    nx=dx
    ny=dy
    while 0<=nx<M-1 and 0<=ny<N-1 and room[ny][nx]!=6:
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
        while 0 <= nx < M-1 and 0 <= ny < N-1 and room[ny][nx] != 6:
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
        while 0 <= nx < M-1 and 0 <= ny < N-1 and room[ny][nx] != 6:
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
        while 0 <= nx < M-1 and 0 <= ny < N-1 and room[ny][nx] != 6:
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
        while 0 <= nx < M-1 and 0 <= ny < N-1 and room[ny][nx] != 6:
            nx = nx + x[dir]
            ny = ny + y[dir]
            if room[ny][nx] == 0:
                room[ny][nx] = 9
            elif room[ny][nx] == 6:
                break
            else:
                continue
    return room


def counting(room_tmp):
    count=0
    for i in range(N):
        for j in range(M):
            if room_tmp[i][j]==0:
                count=count+1
    return count

CCTV_Point=[]
CCTV_Point2=[]
CCTV_Point5=[]

for n in range(N):
    for m in range(M):
        if room[n][m]==5:
            CCTV_Point5.append([m, n])

        elif room[n][m]==1:
            CCTV_Point.append([1,m,n])
        elif room[n][m]==3:
            CCTV_Point.append([3,m,n])
        elif room[n][m]==4:
            CCTV_Point.append([4,m,n])
        elif room[n][m]==2:
            CCTV_Point2.append([m,n])


num4=len(CCTV_Point)
num2=len(CCTV_Point2)

arr4=[0,1,2,3]
arr2=[0,1]

def direction_4(arr4, r):
    for i in range(len(arr4)):
        # i==r이 아니라 r==1인거 조심!!
        if r==1:
            yield [arr4[i]]
        else:
            for next in direction_4(arr4, r-1):
                yield [arr4[i]]+next

def direction_2(arr2, n):
    for i in range(len(arr2)):
        if n==1:
            yield [arr2[i]]
        else:
            for next in direction_2(arr2, n-1):
                yield [arr2[i]]+next

total=[]

if num4!=0 and num2!=0:
    for tmp in direction_4(arr4, num4):
        for tmp2 in direction_2(arr2, num2):
            total_t = tmp + tmp2
            total.append(total_t)

elif num4==0 and num2!=0:
    for tmp2 in direction_2(arr2, num2):
        total.append(tmp2)

elif num4!= 0 and num2==0:
    for tmp in direction_4(arr4, num4):
        total.append(tmp)

print(total)

answer=100
for list_a in total:
    que=deque(list_a)
    room_tmp=copy.deepcopy(room)
    for a in CCTV_Point:
        if a[0]==1:
            CCTV1(room_tmp, a[1], a[2], que.popleft())
        elif a[0]==3:
            CCTV3(room_tmp, a[1], a[2], que.popleft())
        elif a[0]==4:
            CCTV4(room_tmp, a[1], a[2], que.popleft())
    for b in CCTV_Point2:
        CCTV2(room_tmp, b[0], b[1], que.popleft())

    if CCTV_Point5!=0:
        for c in CCTV_Point5:
            CCTV5(room_tmp, c[0], c[1])

    for oh in range(len(room_tmp)):
        print(room_tmp[oh])
    print(counting(room_tmp))
    print(' ')

    if answer>counting(room_tmp):
        answer=counting(room_tmp)


print(answer)

