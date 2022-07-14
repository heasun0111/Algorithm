import sys

left=0
right=0

dx=[1, 1, -1, -1]
dy=[1, -1, -1, 1]

def cafe_route(left, right, cafe):
    answer=[]
    route=[]
    for i in range(N):
        for j in range(N):
            if j-left<0 or j+right>=N or i+left+right>=N:
                continue
            else:
                route.append(cafe[i][j])
                t_i=i
                t_j=j
                for _ in range(right):
                    t_i=t_i+dx[0]
                    t_j=t_j+dy[0]
                    route.append(cafe[t_i][t_j])
                for _ in range(left):
                    t_i=t_i+dx[1]
                    t_j=t_j+dy[1]
                    route.append(cafe[t_i][t_j])
                for _ in range(right):
                    t_i=t_i+dx[2]
                    t_j=t_j+dy[2]
                    route.append(cafe[t_i][t_j])
                for _ in range(left):
                    t_i=t_i+dx[3]
                    t_j=t_j+dy[3]
                    if t_i==i and t_j==j:
                        break
                    route.append(cafe[t_i][t_j])

                set_route=list(set(route))
                if len(route)==len(set_route):
                    if len(answer)<len(route):
                        answer=route
                route = []

    return answer


#모든 경우의 수 구하기
def brute(N, cafe):
    answer=[]
    for i in range(2,N):
        for j in range(1,N-1):
            left=j
            if i-left>=1:
                right=i-left
                tmp=cafe_route(left, right, cafe)
                if len(tmp)>len(answer):
                    answer=tmp

            else:
                continue

    return answer

T=int(input())
for TC in range(1, T+1):
    N=int(input())
    cafe=[list(map(int, input().split())) for _ in range(N)]
    ans=brute(N, cafe)
    if len(ans)==0:
        print('#'+str(TC)+' '+str(-1))
    else:
        print('#'+str(TC)+ ' ' +str(len(ans)))


