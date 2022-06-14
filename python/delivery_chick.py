# 왜 백트래킹이지??

# 입력 받는거 외우기!!
# 두 수, 리스트 공백o, 리스트 공백x

# 조합 결과값 : for 이용하면 리스트처럼 인덱스로 접근 가능!
from itertools import combinations
import copy

N, M = map(int, input().split())
city=[list(map(int, input().split())) for _ in range(N)]

def calDistance(city):
    home=[]
    chick=[]
    for i in range(N):
        for j in range(N):
            if city[j][i]==1:
                home.append([i,j])

            elif city[j][i]==2:
                chick.append([i,j])

    total_dis=0
    for n in home:
        min=101
        for m in chick:
            distance=abs(n[0]-m[0])+abs(n[1]-m[1])
            if distance<min:
                min=distance

        total_dis=total_dis+min

    return total_dis


chickShop=[]
for a in range(N):
    for b in range(N):
        if city[b][a]==2:
            chickShop.append([a,b])

# 조합 이용해서 없앨 매장 경우의 수 모두 구하고
# 함수 이용해서 거리 구하기!!
min_dis=250001
shopCase=combinations(chickShop, len(chickShop)-M)
for tmp in shopCase:
    city_copy=copy.deepcopy(city)
    for p in tmp:
        city_copy[p[1]][p[0]]=0

    ans=calDistance(city_copy)
    if min_dis>ans:
        min_dis=ans

print(min_dis)


'''
for z in shopCase:
    print(z)
    print(z[0][1])
    print(z[1])

'''