# 각 초(M)마다 충전할 수 있는 최대의 양을 파악하고 저장
# 사용자 2명에게 충전기(최대 8개) 범위 파악 -> 충전량 파악 -> 최대값 저장

# index에러 해결!!

def movement(x, y, dir):
    if dir==1:
        y=y+1
    elif dir==2:
        x=x+1
    elif dir==3:
        y=y-1
    elif dir==4:
        x=x-1
    elif dir==0:
        x=x
    return [x,y]

def maxBC(BC_point, A_xy, B_xy, C, P, A, ans):
    A_possible=[]
    B_possible=[]
    for a in range(A):
        if abs(BC_point[a][0]-A_xy[0])+abs(BC_point[a][1]-A_xy[1]) <= C[a]:
            A_possible.append([P[a],a])

        if abs(BC_point[a][0]-B_xy[0])+abs(BC_point[a][1]-B_xy[1]) <= C[a]:
            B_possible.append([P[a],a])

    # A,B 비교해서 최대값 더하는거!
    tmp_A=0
    if len(A_possible)!=0:
        A_possible.sort(reverse=True)
        tmp_A=A_possible[0][0]

    tmp_B=0
    if len(B_possible)!=0:
        B_possible.sort(reverse=True)
        tmp_B=B_possible[0][0]

    if A_possible[0][1]==B_possible[0][1]:
        if len(A_possible)==1 and len(B_possible)>=2:
            ans.append(tmp_A+B_possible[1][0])
        elif len(A_possible)>=2 and len(B_possible)==1:
            ans.append(tmp_B+A_possible[1][0])
        elif len(A_possible)==1 and len(B_possible)==1:
            ans.append(tmp_A)
        else:
            if A_possible[1][0]>B_possible[1][0]:
                ans.append(tmp_B + A_possible[1][0])
            elif A_possible[1][0]<B_possible[1][0]:
                ans.append(tmp_A+B_possible[1][0])
    else:
        ans.append(tmp_A + tmp_B)
    return ans

T=int(input())
for TC in range(1, T+1):
    M, A = map(int, input().split())
    A_move=list(map(int, input().split()))
    B_move=list(map(int, input().split()))

    BC_point=[]
    C=[]
    P=[]
    for i in range(A):
        tmp=list(map(int, input().split()))
        BC_point.append([tmp[0],tmp[1]])
        C.append(tmp[2])
        P.append(tmp[3])

    ans=[]
    A_xy=[1,1]
    B_xy=[10,10]
    ans=maxBC(BC_point, A_xy, B_xy, C, P, A, ans)

    for k in range(M):
        A_xy=movement(A_xy[0], A_xy[1], A_move[k])
        B_xy=movement(B_xy[0], B_xy[1], B_move[k])
        ans = maxBC(BC_point, A_xy, B_xy, C, P, A, ans)

    if len(ans)==0:
        print('#'+str(TC)+' '+str(-1))
    else:
        print('#'+str(TC)+ ' ' +str(len(ans)))