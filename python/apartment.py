#BFS버젼
from collections import deque

N=int(input())
apart=[]

#입력 (여기서는 토마토와 다르게 공백 없이 받는다)
for _ in range(N):
    apart.append(list(map(int,input())))

q=deque()

def BFS(x,y,cnt):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    q.append([x,y])
    while q:
        a, b=q.popleft()
        apart[a][b]=0
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<N and apart[nx][ny]==1:
                q.append([nx, ny])
                apart[nx][ny]=0
                cnt=cnt+1

    return cnt


answer=[]
for i in range(N):
    for j in range(N):
        if apart[i][j]==1:
            cnt=1
            cnt=BFS(i,j,cnt)
            answer.append(cnt)


answer.sort()
print(len(answer))
for k in answer:
    print(k)

# 어디를 고친거고 왜 맞게된건지
# q에서 뺄 때도 apart[a][b]=0 으로 바꿔주고 nx, ny에 대해서도 0으로 바꾸준다 (중복 카운팅 생길 수 있음)

"""
처음에 고려 못한 테스트 케이스 - (단지가 1개일때, 시작부분)
3
010
101
010
cnt=0으로 시작해서 이 경우 0이 4번 카운팅 됨
"""
