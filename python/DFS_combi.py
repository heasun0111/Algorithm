l = ['a', 'b', 'c', 'd']
#r = 3
answer = []

def dfs(idx, list):
    if len(list) == 3:
        answer.append(list[:])
        return

    for i in range(idx, len(l)):
        print(i)
        dfs(i+1,list+[l[i]])

dfs(0, [])
print(answer)