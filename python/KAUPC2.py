import itertools

N, K=map(int,input().split())

A=[list(map(int, input().split()))]
R=[list(map(int, input().split())) for _ in range(N)]
M=[list(map(int, input().split())) for _ in range(N)]

def giveCan(n):
    if n>=0 and n<N:
        flag=True
        for i in range(N-1):
            if R[n][i]!=R[n][i+1]:
                flag=False

        tmp_ans=-1
        tmp_idx=-1
        if flag==False:
            for j in range(K):
                if R[n][j]>tmp_ans and A[j]!=0:
                    tmp_ans=R[n][j]
                    tmp_idx=j

            A[tmp_idx]=A[tmp_idx]-1
            return tmp_ans

        else:
            return -1

    elif n>=N and n<2*N:
        flag = True

        for i in range(n - N - 1):
            if M[n- N][i] != M[n- N][i + 1]:
                flag = False

        tmp_ans = -1
        tmp_idx = -1
        if flag == False:
            for j in range(K):
                if M[n- N][j] > tmp_ans and A[j] != 0:
                    tmp_ans = M[n- N][j]
                    tmp_idx = j

            A[tmp_idx] = A[tmp_idx] - 1
            return tmp_ans

        else:
            return -1

ans=0
# i랑 K+i
for num in itertools.permutations(range(2*N), 2*N):
    temp_ans=0
    for i in num:
        if giveCan(i)==-1:
            if i>=0 and i<N:
                temp_ans = temp_ans + R[i][0]
            elif i>=N and i<2*N:
                temp_ans = temp_ans + M[i-N][0]
        else:
            temp_ans = temp_ans+giveCan(i)

    if temp_ans>ans:
        ans=temp_ans

print(ans)








