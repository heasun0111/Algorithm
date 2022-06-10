import math

N=int(input())

server=[list(map(int, input().split())) for _ in range(N)]

computer=[0 for _ in range(10000000)]

def binary_search(arr, last_idx, value):
    first=0
    last=last_idx

    while first<=last:
        mid=(first+last)//2
        if arr[mid]==value:
            return mid

        if arr[mid]>value:
            last=mid-1
        else:
            first=mid+1

    return mid

last_idx=0
for i in range(N):
    for j in range(N):
        if server[j][i]>last_idx:
            last_idx=server[j][i]

        if server[j][i]!=0:
            computer[server[j][i]] = computer[server[j][i]] + 1
        else:
            continue

computer_tmp=[0 for _ in range(last_idx)]
computer_C=[0 for _ in range(last_idx)]
#computer 누적 다시 구하기 -> 1층에 깔린거 생각!!
for i in range(last_idx-1):
    computer_tmp[i+1]=computer_tmp[i]+computer[i+1]*(i+1)

total_com=computer_tmp[last_idx]

computer_C[0]=total_com
computer_C[1]=total_com
#for i in range(1,last_idx-1):

val=math.ceil(computer_C[last_idx]/2)

result=binary_search(computer_C[:last_idx+1], last_idx, val)
print(result)

