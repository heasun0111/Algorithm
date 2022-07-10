
r, n = map(int, input().split())
arr4=[0,1,2,3]
arr2=[0,1]

def direction_4(arr4, r):
    for i in range(len(arr4)):
        # i==r이 아니라 r==1인거 조심!!
        if r==1:
            yield [arr4[i]]
        else:
            for next in direction_4(arr4, r-1):
                yield [arr4[i]]+next

def direction_2(arr2, n):
    for i in range(len(arr2)):
        if n==1:
            yield [arr2[i]]
        else:
            for next in direction_2(arr2, n-1):
                yield [arr2[i]]+next

for tmp in direction_4(arr4, r):
    print(tmp)

for tmp2 in direction_2(arr2, n):
    print(tmp2)

for tmp3 in direction_4(arr4, r):
    for tmp4 in direction_2(arr2, n):
        print(tmp3+tmp4)