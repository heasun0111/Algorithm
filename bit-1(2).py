import sys
import math

T=int(input())

for j in range(1,T+1):
    N=int(input())
    N_ori=N

    masking=0
    cnt=0
    multi=1
    
    while(masking!=0b1111111111):
        tmp=str(N)
        for i in range(len(tmp)):
            num=int(tmp[i])
            bit=1<<num
            masking|=bit
        
        if(masking==0b1111111111):
            break

        cnt=cnt+1
        N=N_ori*(cnt+1)

    print('#'+str(j)+' '+str(N))

# for문에서 i를 두 번 써서, 마지막 for문의 i를 출력함
# 출력해야하는 값이 cnt가 아니라 N이었음
# 출력 양식 #1 맞추기
