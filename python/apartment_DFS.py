#DFS버젼
N=int(input())
apart=[]
cnt=1

#입력
for _ in range(N):
    apart.append(list(map(int,input())))

def DFS(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    apart[x][y]=0
    global cnt
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and apart[nx][ny]==1:
            apart[nx][ny]=0
            cnt=cnt+1
            DFS(nx, ny)


answer=[]
for n in range(N):
    for m in range(N):
        if apart[n][m]==0:
            continue
        elif apart[n][m]==1:
            cnt=1
            DFS(n,m)
        answer.append(cnt)


answer.sort()
print(len(answer))
for k in answer:
    print(k)


# cnt를 global로 선언!
# cnt위치!!