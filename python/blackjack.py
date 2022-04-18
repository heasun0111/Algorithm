
N, M= map(int,input().split())
arr = list(map(int,input().split()))

tmp=[]
def DFS(idx, list):
    if len(list)==3:
        tmp.append(list[:])
        return

    for i in (idx, N):
        DFS(i+1, list+[arr[i]])

#DFS에 넣는거 빈 배열
DFS(0,[])
print(tmp)