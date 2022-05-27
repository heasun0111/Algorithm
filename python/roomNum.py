import math

N=input()
set=[0,0,0,0,0,0,0,0,0]

for i in range(len(N)):
    if int(N[i])==6 or int(N[i])==9:
        set[6]=set[6]+1
    else:
        set[int(N[i])]=set[int(N[i])]+1

set[6]=math.ceil(set[6]/2)

print(max(set))