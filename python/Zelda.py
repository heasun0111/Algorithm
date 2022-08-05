import heapq

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
INF=int(1e9)

def dijkstra():
    q=[]
    heapq.heappush(q, (graph[0][0], 0,0))
    distance[0][0]=0

    while q:
        cost, x, y = heapq.heappop(q)
        if x==N-1 and y==N-1:
            print('Problem '+str(count)+': '+str(distance[x][y]))
            break

        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 0<=next_x<N and 0<=next_y<N:
                next_cost=cost+graph[next_x][next_y]
                # 들여쓰기 조심!
                if next_cost<distance[next_x][next_y]:
                    distance[next_x][next_y]=next_cost
                    # heappush할 때, q도 입력하는거랑
                    # distance대신 new_cost 넣는거 주의!!
                    heapq.heappush(q, (next_cost, next_x, next_y))


N=int(input())
count=1
while N!=0:
    graph=[list(map(int, input().split())) for _ in range(N)]
    distance=[[INF]*N for _ in range(N)]
    dijkstra()
    count=count+1
    N=int(input())