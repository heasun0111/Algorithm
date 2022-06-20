
N=int(input())
file={}

for _ in range(N):
    tmp=input()
    idx=tmp.index('.')
    file_name=tmp[idx+1:]

    if file_name not in file:
        file[file_name]=1

    else:
        file[file_name]=file[file_name]+1

ans=[]

# file.items하고서 괄호()  필수!!!
for key in file.items():
    ans.append(key)
    #key를 넣었는데 value까지 다 들어가네...?

#sort()하니까 ans내용이 바뀌네 -> 굳이 = 할 필요x
ans.sort()
for i in ans:
    print(i[0]+' '+str(i[1]))