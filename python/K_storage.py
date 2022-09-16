# 레일은 큐, 적재 공간은 스택
# 우선 순위 처리하는거 -> 배열 이용해서 개수 카운팅! -> 0되면 다음 우선순위로 넘어가기!!
# 배열 insert는 원하는 위치에 추가!
# 초기화 2번 선언해서 틀렸었음! (주의!!)


# 큐
rail=[]
# 스택
load=[]

N, M = map(int, input().split())
priority=[0 for _ in range(M+1)]

for _ in range(N):
    P, W = map(int,input().split())
    rail.append([P,W])
    priority[P]=priority[P]+1

ans=0
now=M
while rail:
    for i in range(len(rail)):
        if priority[now] == 0:
            now = now - 1
            load = []
        pri, wei=rail.pop(0)
        if pri<now:
            rail.append([pri, wei])
            ans=ans+wei

        elif pri==now:
            if len(load)==0:
                load.append([pri, wei])
                priority[now]=priority[now]-1
                ans=ans+wei
            else:
                if load[-1][1]>=wei:
                    load.append([pri, wei])
                    priority[now] = priority[now] - 1
                    ans=ans+wei
                else:
                    Flag=False
                    tmp=0
                    for i in range(len(load)):
                        if load[i][1]<wei and Flag==False:
                            ans=ans+load[i][1]*2
                            tmp=i
                            Flag==True
                        elif load[i][1]<wei and Flag==True:
                            ans=ans+load[i][1] * 2
                        else:
                            continue
                    ans=ans+wei
                    load.insert(tmp, [pri, wei])
                    priority[now]=priority[now]-1

print(ans)








