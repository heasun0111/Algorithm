#import sys
from collections import deque

deque1=deque()
ans=[]


N, K=map(int,input().split())
#N, K = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    deque1.append(i)
    

while len(ans)<N:        
    for i in range(K-1):        
        tmp=deque1.popleft()
        deque1.append(tmp)
    ans.append(str(deque1.popleft()))


string=", ".join(ans)

print('<'+string+'>')        
