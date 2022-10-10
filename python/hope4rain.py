# 모듈러(%)연산은 음수도 양수로 변환 가능!! -> 배열 연결 시 유용
# for y, x in moved_clouds: 이용해서 배열 속 배열[x, y] 깔끔하게 꺼내기!
# 좌표 x, y 순서 체크!
# 전역변수 이용하기 싫어서 함수로 안만든 듯?
# 시간초과,,, -> 왜일까?

dx=[0, 0, -1, -1, -1, 0, 1, 1, 1]
dy=[0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]

cld=[[N-1,0], [N-1,1], [N-2,0], [N-2,1]]
plusW=[]

def makeCloud(d,s):
    global cld
    global plusW

    for x, y in cld:
        Nx = (x + dx[d]*s) % N
        Ny = (y + dy[d]*s) % N
        basket[Nx][Ny] = basket[Nx][Ny] + 1
        plusW.append([Nx, Ny])
        # 굳이 plusW 안쓰고 cld만 써도 될듯?

def copyWater():
    global plusW
    for x, y in plusW:
        cnt=0
        if x-1>=0 and x-1<N and y-1>=0 and y-1<N and basket[x-1][y-1]>0:
            cnt = cnt+1
        if x-1>=0 and x-1<N and y+1>=0 and y+1<N and basket[x-1][y+1]>0:
            cnt = cnt+1
        if x+1>=0 and x+1<N and y+1>=0 and y+1<N and basket[x+1][y+1]>0:
            cnt = cnt+1
        if x+1>=0 and x+1<N and y-1>=0 and y-1<N and basket[x+1][y-1]>0:
            cnt = cnt+1

        basket[x][y]=basket[x][y]+cnt


def newCloud():
    global cld
    global plusW

    tmp_cld=[]
    for i in range(N):
        for j in range(N):
            if [i,j] in plusW or basket[i][j]<2:
                continue
            basket[i][j]=basket[i][j]-2
            tmp_cld.append([i,j])

    plusW.clear()
    cld.clear()
    cld=tmp_cld

for _ in range(M):
    d, s=map(int, input().split())
    makeCloud(d, s)
    copyWater()
    newCloud()


ans=0
for a in range(N):
    for b in range(N):
        ans=ans+basket[a][b]

print(ans)



# 구현 문제 -> 일단 구현 -> 후 고침!!



'''
배열 값 삭제
str.clear() -> 모든 값 삭제
str.pop(2) -> 취득 후 삭제
str.remove('a') -> 요소 찾아서 삭제
del str[1] -> 인덱스/슬라이스로 범위 지정 삭제

'''
