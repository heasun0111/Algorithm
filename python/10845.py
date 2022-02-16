import sys

queue=[]

N=int(sys.stdin.readline())

h_idx=0

for _ in range(N):
    tmp=sys.stdin.readline().strip()
    tmp=tmp.split()

    if tmp[0]=="push":
        queue.append(tmp[1])
    
    elif tmp[0]=="pop":
        if len(queue)==0:
            print(-1)
            
        else:
            print(queue[h_idx])
            queue.pop(h_idx)

    elif tmp[0]=="size":
        print(len(queue))


    elif tmp[0]=="empty":
        if len(queue)==0:
            print(1)
            
        else:
            print(0)    
            

    elif tmp[0]=="front":
        if len(queue)==0:
            print(-1)

        else:
            print(queue[h_idx])


    elif tmp[0]=="back":
        if len(queue)==0:
            print(-1)

        else:
            t_idx=len(queue)-1
            print(queue[t_idx])
    
