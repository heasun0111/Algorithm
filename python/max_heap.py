import heapq
import sys

N=int(input())
heap=[]

for _ in range(N):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        if len(heap)==0:
            print('0')
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (-tmp, tmp))
