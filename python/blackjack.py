#조합 이용해서 완전탐색 한 후 가장 작은 차이 합을 출력

N, M= map(int,input().split())
arr = list(map(int,input().split()))

tmp=[]
def DFS(idx, list):
    if len(list)==3:
        tmp.append(list[:])
        return

    #range 빼먹지 말기!
    for i in range(idx, N):
        DFS(i+1, list+[arr[i]])

#DFS에 넣는거 빈 배열
DFS(0,[])

min=300000
ans_idx=-1

for j in range(len(tmp)):
    if sum(tmp[j])<=M and M-sum(tmp[j])<min:
        min=M-sum(tmp[j])
        ans_idx=j

print(sum(tmp[ans_idx]))
