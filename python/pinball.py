# 맵 밖으로 나가는 것을 5블록으로 감싸는 것으로 처리!
# 웜홀 딕셔너리 이용해서 양쪽으로 처리 -> 굳이 번호대로 입력할 필요 없다!
# 굳이 블랙홀은 append 할 필요는 없을듯!

dir_x=[0,-1,0,1]
dir_y=[1,0,-1,0]

block=[
    [],
    [3,2,0,1],
    [2,0,3,1],
    [2,3,1,0],
    [1,3,0,2],
    [2,3,0,1]
]

def gameStart(game, i, j, d):
    global black_hole
    global worm6
    global worm7
    global worm8
    global worm9
    global worm10

    start_x=i
    start_y=j

    x=start_x+dir_x[d]
    y=start_y+dir_y[d]
    tmp_score=0
    while (x!=start_x and y!=start_y) and ([x,y] not in black_hole):
        if x<0:
            x=0
            d=(d+2)%4
            tmp_score = tmp_score + 1
        elif y<0:
            y=0
            d=(d+2)%4
            tmp_score = tmp_score + 1
        elif x>=N:
            x=N-1
            d=(d+2)%4
            tmp_score = tmp_score + 1
        elif y>=N:
            y=N-1
            d=(d+2)%4
            tmp_score = tmp_score + 1

        else:
            if game[x][y] == 0:
                x = start_x + dir_x[d]
                y = start_y + dir_y[d]

            elif game[x][y] == 1 or game[x][y] == 2 or game[x][y] == 3 or game[x][y] == 4 or game[x][y] == 5:
                d = block[game[x][y]][d]
                tmp_score = tmp_score + 1
                x = start_x + dir_x[d]
                y = start_y + dir_y[d]

            elif game[x][y] == 6:
                if worm6[0][0]==x and worm6[0][1]==y:
                    x=worm6[1][0]+dir_x[d]
                    y=worm6[1][1]+dir_y[d]
                else:
                    x=worm6[0][0]+dir_x[d]
                    y=worm6[0][1]+dir_y[d]

            elif game[x][y] == 7:
                if worm7[0][0]==x and worm7[0][1]==y:
                    x=worm7[1][0]+dir_x[d]
                    y=worm7[1][1]+dir_y[d]
                else:
                    x=worm7[0][0]+dir_x[d]
                    y=worm7[0][1]+dir_y[d]

            elif game[x][y] == 8:
                if worm8[0][0]==x and worm8[0][1]==y:
                    x=worm8[1][0]+dir_x[d]
                    y=worm8[1][1]+dir_y[d]
                else:
                    x=worm8[0][0]+dir_x[d]
                    y=worm8[0][1]+dir_y[d]

            elif game[x][y] == 9:
                if worm9[0][0]==x and worm9[0][1]==y:
                    x=worm9[1][0]+dir_x[d]
                    y=worm9[1][1]+dir_y[d]
                else:
                    x=worm9[0][0]+dir_x[d]
                    y=worm9[0][1]+dir_y[d]

            elif game[x][y] == 10:
                if worm10[0][0]==x and worm10[0][1]==y:
                    x=worm10[1][0]+dir_x[d]
                    y=worm10[1][1]+dir_y[d]
                else:
                    x=worm10[0][0]+dir_x[d]
                    y=worm10[0][1]+dir_y[d]

    return tmp_score

T = int(input())
for tc in range(1, T + 1):
    N=int(input())
    game=[list(map(int, input().split())) for _ in range(N)]

    black_hole=[]
    worm6=[]
    worm7=[]
    worm8=[]
    worm9=[]
    worm10=[]

    for a in range(N):
        for b in range(N):
            if game[a][b]==-1:
                black_hole.append([a,b])
            elif game[a][b]==6:
                worm6.append([a,b])
            elif game[a][b]==7:
                worm7.append([a,b])
            elif game[a][b]==8:
                worm8.append([a,b])
            elif game[a][b]==9:
                worm9.append([a,b])
            elif game[a][b]==10:
                worm10.append([a,b])

    answer=0
    for i in range(N):
        for j in range(N):
            if game[i][j]==0:
                for d in range(4):
                    score=gameStart(game, i, j, d)
                    if score>answer:
                        answer=score
    print('#'+str(tc)+' '+str(answer))
