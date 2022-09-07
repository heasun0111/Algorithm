# 교차로를 어떤 자료구조 써서 구현? -> 더 간단하게!
# FIFO이라서 큐 써야한다!

N=int(input())
ans=[0 for _ in range(N)]
A=[]
B=[]
C=[]
D=[]

for i in range(N):
    t, w=map(int, input().split())
    if w=='A':
        A.append([i,t])
    elif w=='B':
        B.append([i,t])
    elif w=='C':
        C.append([i,t])
    elif w=='D':
        D.append([i,t])


def cal_interS():




flag=True
while flag==True:



