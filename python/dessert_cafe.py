import sys

left=0
right=0

dx=[1, -1, -1, 1]
dy=[1, 1, -1, -1]

def cafe_route(left, right, cafe):
    answer=[]
    route=[]
    for i in range(N):
        for j in range(N):
            if j-left<0 or j+right>N or i+left+right>N:
                continue
            else:
                route.append(cafe[i][j])
                for _ in range(right):
                    i=i+dx[0]
                    j=j+dx[0]
                    route.append(cafe[i][j])
                for _ in range(left):
                    i=i+dx[1]
                    j=j+dx[1]
                    route.append(cafe[i][j])
                for _ in range(right):
                    i=i+dx[2]
                    j=j+dx[2]
                    route.append(cafe[i][j])
                for _ in range(left):
                    i=i+dx[3]
                    j=j+dx[3]
                    route.append(cafe[i][j])

                set_route=list(set(route))
                if len(route)==set_route:
                    if len(answer)<len(route):
                        answer=route
    return answer


#모든 경우의 수 구하기
def brute(N, cafe):
    answer=[]
    for i in range(2,N):
        for j in range(1,N-1):
            left=j
            if i-left>=1:
                right=i-left
                answer=cafe_route(left, right, cafe)
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
        print('#'+str(TC)+ ' ' +str(ans))


