# 이진수 이용해서 1씩 더하면서 1의 개수가 K가 되도록하는 최솟값 구하기!
# -1인 경우...?
# 시간초과!!

N, K=map(int, input().split())

# bin()함수를 이용하면 이미 문자열로 변환
bottle=bin(N)
ans=0
total_1=0
for i in range(len(bottle)):
    if bottle[i]=='1':
        total_1=total_1+1
    else:
        continue

while total_1!=K:
    #2진수 문자열을 다시 10진수로 변환
    bottle_num=int(bottle, 2)
    bottle_num=bottle_num+1
    ans=ans+1
    bottle = bin(bottle_num)

    total_1=0
    for i in range(len(bottle)):
        if bottle[i] == '1':
            total_1 = total_1 + 1
        else:
            continue

print(ans)

