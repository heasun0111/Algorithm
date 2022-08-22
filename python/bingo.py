
bingo=[list(map(int, input().split())) for _ in range(5)]
ans=[list(map(int, input().split())) for _ in range(5)]

visited=[[0 for _ in range(5)]for _ in range(5)]

def find_bingo(visited):
    bingo=0
    for a in range(5):
        flag=True
        for b in range(5):
            if visited[a][b]==0:
                flag=False
        if flag==True:
            bingo=bingo+1

    for c in range(5):
        flag=True
        for d in range(5):
            if visited[d][c]==0:
                flag=False
        if flag==True:
            bingo=bingo+1

    for e in range(5):
        flag=True
        if visited[e][e]==0:
            flag=False
    if flag == True:
        bingo = bingo + 1

    for f in range(5):
        flag=True
        if visited[4-f][f]==0:
            flag=False
    if flag == True:
        bingo = bingo + 1

    if bingo>=3:
        print('야옹~~')
        for z in range(5):
            print(visited[z])
        return True
    else:
        return False

def check_bingo(bingo, visited, num):
    for i in range(5):
        for j in range(5):
            if num==bingo[i][j]:
                visited[i][j]=1
    return visited

answer=0
for i in range(5):
    for j in range(5):
        answer=answer+1
        check_bingo(bingo, visited, ans[i][j])
        if find_bingo(visited)==True:
            print(answer)
            break
            break



