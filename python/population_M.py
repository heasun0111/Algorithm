# BFS 이용하면 굳이 경계선 안해도 될 듯?
N, L, R = map(int, input().split())
A=[list(map(int, input().split())) for _ in range(N)]

line=[[0 for _ in range(N)]for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

#def bfs(A):

def find_open(A):
    cnt=0
    for i in range(N):
        for j in range(N):
            for a in range(4):
                nx=i+dx[a]
                ny=j+dy[a]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                else:
                    if abs(A[i][j]-A[nx][ny])>=L and abs(A[i][j]-A[nx][ny])<=R:
                        if line[i][j]==0 and line[nx][ny]==0:
                            line[i][j]=cnt
                            line[nx][ny]=cnt
                            cnt=cnt+1
                        # 서로 다른 영역에서 오픈된 두 영역이 연결될 때!

