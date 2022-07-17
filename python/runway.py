# 경사로 중복되는 경우 어케 처리할지 생각!

N, L = map(int, input().split())
runway=[list(map(int, input().split())) for _ in range(N)]
visited=[[0 for _ in range(N)]for _ in range(N)]

ans=0
for j in range(N):
    flag=True
    for i in range(N-1):
        if abs(runway[j][i]-runway[j][i+1])>1:
            flag=False
            break

        elif runway[j][i]-runway[j][i+1] == 1:
            visited[j][i+1]=1
            for k in range(1,L):
                if i+1+k>=N:
                    flag=False
                    break

                if runway[j][i+1] != runway[j][i+1+k]:
                    flag = False
                    break

                # 경사로 넣는거 구현!! -> 경우의 수 고려
                elif visited[j][i+1]!=0 and visited[j][i+1+k]!=0:
                    flag = False

                else:
                    visited[j][i+1+k]=k+1


        elif runway[j][i]-runway[j][i+1] == -1:
            for k in range(1,L):
                if i-k < 0:
                    flag=False
                    break
                if runway[j][i] != runway[j][i-k]:
                    flag=False
                    break

        elif runway[j][i]-runway[j][i+1]==0:
            continue

    if flag==True:
        ans=ans+1

for j in range(N):
    flag = True
    for i in range(N - 1):
        if abs(runway[i][j] - runway[i + 1][j]) > 1:
            flag = False
            break

        elif runway[i][j] - runway[i + 1][j] == 1:
            for k in range(1, L):
                if i + 1 + k >= N:
                    flag = False
                    break
                if runway[i + 1][j] != runway[i + 1 + k][j]:
                    flag = False
                    break

        elif runway[i][j] - runway[i + 1][j] == -1:
            for k in range(1, L):
                if i - k < 0:
                    flag = False
                    break
                if runway[i][j] != runway[i - k][j]:
                    flag = False
                    break

        elif runway[i][j] - runway[i + 1][j] == 0:
            continue

    if flag == True:
        ans = ans + 1

print(ans)
