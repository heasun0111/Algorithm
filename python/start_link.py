# 조합 이용해서 팀 나누고
# 나눈 팀 점수 차이 다 구해서
# 최소값 구하기!!

N=int(input())
team=[list(map(int, input().split())) for _ in range(N)]

def combi(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            # 슬라이싱 잊지말기!!
            for next in combi(arr[i+1:], r-1):
                yield [arr[i]]+next

# range앞에 list붙이기
min=10000
for tmp in combi(list(range(N)), N/2):
    ability_A=0
    ability_B=0
    for a in tmp:
        for b in tmp:
            ability_A=ability_A+team[a][b]

    tmp_B=[]
    for k in range(N):
        if k not in tmp:
            tmp_B.append(k)
        else:
            continue

    for c in tmp_B:
        for d in tmp_B:
            ability_B = ability_B + team[c][d]

    if abs(ability_A-ability_B)<min:
        min=abs(ability_A-ability_B)


print(min)

