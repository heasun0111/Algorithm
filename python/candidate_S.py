from collections import deque

N=int(input())
T=int(input())

S=list(map(int, input().split()))

student=deque()
counting=deque()

for i in S:
    if len(student)<N:
        


