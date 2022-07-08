# Python3으로 제출하면 시간 초과 -> PyPy3으로 제출했더니 통과!!

import math

N=int(input())
num=[]
for _ in range(N):
    number=int(input())
    num.append(number)

# 여기서 시간 초과?
num.sort()

dic={
}

for tmp in num:
    if tmp not in dic:
        dic[tmp]=1
    else:
        dic[tmp]=dic[tmp]+1


aver=sum(num)/N
# 산술평균
print(round(aver))

M=int((N-1)/2)
median=num[M]
# 중앙값
print(median)

fre=0
fre_value=[]
for value, key in dic.items():
    if key>fre:
        fre=key
    else:
        continue

for value, key in dic.items():
    if key==fre:
        fre_value.append(value)

# 최빈값
if len(fre_value)==1:
    print(fre_value[0])

else:
    fre_value.sort()
    print(fre_value[1])

# 범위
print(abs(num[-1]-num[0]))


