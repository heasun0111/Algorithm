
N=int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

for _ in range(N):
    tmp=input()

    # 반복문 시작하면 초기화!!
    t_x, t_y = 0, 0
    idx = 0
    road_x = [0]
    road_y = [0]
    for i in range(len(tmp)):
        if tmp[i]=='F':
            t_x=t_x+dx[idx]
            t_y=t_y+dy[idx]
            road_x.append(t_x)
            road_y.append(t_y)

        elif tmp[i]=='B':
            t_x=t_x-dx[idx]
            t_y=t_y-dy[idx]
            road_x.append(t_x)
            road_y.append(t_y)

        elif tmp[i]=='L':
            idx=idx-1
            if idx<0:
                idx=idx+4

        elif tmp[i]=='R':
            idx=idx+1
            if idx>3:
                idx=idx-4

    road_x.sort()
    road_y.sort()
    answer=abs(road_x[-1]-road_x[0])*abs(road_y[-1]-road_y[0])
    print(answer)
