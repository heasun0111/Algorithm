from collections import deque
# x랑 y 순서 헷갈리지 말기!
# 처음과 끝에서 index에러 뜨는듯;;

N=int(input())

K=int(input())
apple=[]
if K!=0:
    for i in range(K):
        a, b = map(int, input().split())
        apple.append([a, b])

L=int(input())
dir=deque()
for j in range(L):
    c,d=input().split()
    dir.append([int(c),d])

snake=deque()
H_x, H_y = 1, 1

dx=[0,1,0,-1]
dy=[1,0,-1,0]
idx_d=0

cnt=0
snake.append([H_x,H_y])
flag=True
while(flag==True):
    #뱀 머리 방향
    if len(dir)>0:
        tmp_dir=dir[0]
        if cnt == tmp_dir[0]:
            if tmp_dir[1] == 'D':
                idx_d = idx_d + 1
            elif tmp_dir[1] == 'L':
                idx_d = idx_d - 1
            dir.popleft()

    cnt=cnt+1
    H_x=H_x+dx[idx_d]
    H_y=H_y+dy[idx_d]

    #외곽에 쿵
    if H_x<1 or H_x>N or H_y<1 or H_y>N:
        flag=False
        break

    #자기 몸에 쿵
    for k in range(len(snake)):
        if snake[k][0]==H_x and snake[k][1]==H_y:
            flag=False
            break

    snake.append([H_x, H_y])

    flag_apple=False
    if len(apple)>0:
        for n in range(len(apple)):
            if apple[n][0] == H_x and apple[n][1] == H_y:
                apple[n][0] = 0
                apple[n][1] = 0
                flag_apple = True
            else:
                continue

    if flag_apple==False:
        snake.popleft()
    else:
        continue

print(cnt)




