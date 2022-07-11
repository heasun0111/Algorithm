from collections import deque

gear1=input()
gear2=input()
gear3=input()
gear4=input()

gear1=deque(gear1)
gear2=deque(gear2)
gear3=deque(gear3)
gear4=deque(gear4)

def clock():

K=int(input())
for _ in range(K):
    n, m=map(int, input().split())


