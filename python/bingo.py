bingo=[list(map(int, input().split())) for _ in range(5)]
ans=[list(map(int, input().split())) for _ in range(5)]

visited=[[0 for _ in range(5)]for _ in range(5)]
def find_bingo(visited):
    bingo=0
    for g in range(5):
        flag=True
        for h in range(5):
            if visited[g][h]==0:
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

    flag=True
    for e in range(5):
        if visited[e][e]==0:
            flag=False
    if flag == True:
        bingo = bingo + 1

    flag=True
    for f in range(5):
        if visited[4-f][f]==0:
            flag=False
    if flag == True:
        bingo = bingo + 1

    if bingo>=3:
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
a=0
b=0
while a<5:
    answer=answer+1
    check_bingo(bingo, visited, ans[a][b])
    if find_bingo(visited)==True:
        print(answer)
        break
    b=b+1
    if b==5:
        a=a+1
        b=0