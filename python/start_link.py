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
for tmp in combi(list(range(N)), N/2):
    print(tmp)

