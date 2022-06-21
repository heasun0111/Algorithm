# 비스마스킹을 이용해서 하나하나 다 해보기 -> 2^10 밖에 안되서 시간초과 문제 없음
import itertools

N=int(input())
sour=[]
bitter=[]

for _ in range(N):
    # .split()에서 괄호 조심!!
    S,B=map(int, input().split())
    sour.append(S)
    bitter.append(B)

# 중복조합 스스로 구현하는거 연습!!
bitmask=itertools.product([0,1], repeat=N)

min=1000000000
for tmp in bitmask:
    if 1 not in tmp:
        continue

    else:
        tmp_S = 1
        tmp_B = 0
        for i in range(N):
            if tmp[i] == 1:
                tmp_S = tmp_S * sour[i]
                tmp_B = tmp_B + bitter[i]
            else:
                continue

        if abs(tmp_S - tmp_B) < min:
            min = abs(tmp_S - tmp_B)

print(min)



