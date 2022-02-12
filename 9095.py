import sys

arr=[1,2,4,0,0,0,0,0,0,0,0]
    

T=int(input())
for _ in range(T):
    n=int(input())
    
    if n<4:
        print(arr[n])

    else:
        for i in range(n-2):
            arr[i+3]=arr[i]+arr[i+1]+arr[i+2]
            print(arr[n])
        print(arr[n])
        
