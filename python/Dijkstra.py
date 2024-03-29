# 우선순위 큐 이용해서 시간복잡도 줄인 다익스트라
import heapq
import sys

input=sys.stdin.readline()
INF=int(1e9)

n, m = map(int, input().split())
start = int(input())
distance = [INF]*(n+1)

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])


'''
import sys

input=sys.stdin.readline
INF=int(1e9)

n, m = map(int, input().split())
start=int(input())
visited=[False]*(n+1)
distance=[INF]*(n+1)

graph=[[] for i in range(n+1)]

for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for j in range(start):
        distance[j[0]]=j[1]

    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[1]
        if cost<distance[j[0]]:
            distance[j[0]]=cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])

'''
