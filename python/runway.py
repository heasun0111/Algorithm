
N, L = map(int, input().split())
runway=[list(map(int, input().split())) for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]

ans=0
for j in range(N):
    flag=True
    for i in range(N-1):
        if abs(runway[j][i]-runway[j][i+1])>1:
            flag=False
            break
        elif runway[j][i]-runway[j][i+1]==1 and visited[j][i]==0 and visited[j][i+1]==0:
            visited[j][i+1]=1
            #방문 표시한거 다시 초기화
            for k in range(1,L):
                if i+1+k>=N:
                    flag=False
                    break
                if runway[j][i+1]!=runway[j][i+1+k]:
                    flag=False
                    break
                else:
                    visited[j][i+1+k]=1

        elif runway[j][i]-runway[j][i+1]==-1 and visited[j][i]==0 and visited[j][i+1]==0:
            visited[j][i]=1
            for k in range(1,L):
                if i+1+k>=N:
                    flag=False
                    break
                if runway[j][i+1]!=runway[j][i+1+k]:
                    flag=False
                    break
                else:
                    visited[j][i+1+k]=1
        elif runway[j][i]-runway[j][i+1]==0:
            continue
    if flag==True:
        ans=ans+1

for j in range(N):
    flag = True
    for i in range(N-1):
        if abs(runway[i][j] - runway[i + 1][j]) > 1:
            flag=False
            break

        elif runway[i][j]-runway[i + 1][j]==1 and visited[j][i]==0 and visited[j][i+1]==0:
            visited[j][i]=1
            for k in range(1, L):
                if i + 1 + k >= N:
                    flag = False
                    break
                if runway[i + 1][j] != runway[i + 1 + k][j]:
                    flag = False
                    break
                else:
                    visited[j][i+1+k]=1

        elif runway[i][j]-runway[i + 1][j]==-1  and visited[j][i]==0 and visited[j][i+1]==0:
            visited[j][i] = 1
            for k in range(1, L):
                if i - k < 0:
                    flag = False
                    break
                if runway[i][j] != runway[i - k][j]:
                    flag = False
                    break
                else:
                    visited[j][i+1+k]=1

        elif runway[i][j]-runway[i + 1][j] == 0:
            continue

    if flag==True:
        ans=ans+1

for j in range(N):
    print(visited[j])

print(ans)
