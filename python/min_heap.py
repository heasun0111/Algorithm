# 시간초과나면 sys이용해서 입력 받는다!!
from queue import PriorityQueue
import sys

N=int(input())
que=PriorityQueue()

for _ in range(N):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        if que.qsize()==0:
            print('0')
        else:
            print(que.get())

    elif tmp!=0:
        que.put(tmp)


# PriorityQueue와 heapq의 차이점
# Thread-safe와 Non-safe의 차이점을 가지고 있다.
# 그러나 safe과정에서 시간이 더 걸려서 heapq가 더 빠르다
# 따라서 코테에서는 heaqp를 더 추천!!
