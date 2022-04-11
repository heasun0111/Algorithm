#파이썬 입력도 공부하자!!
a, b = map(int, input().strip().split(' '))
chess=[]

for _ in range(a):
    chess.append(input())

# %이용해서 flag 없이 구현 가능
def checkNum(x,y):
    minN=-1
    cnt=0
    flag=True
    for k in range(8):
        for l in range(8):
            if flag==True:
                if chess[x + k][y + l]!='B':
                    chess[x + k][y + l] = 'B'
                    cnt=cnt+1
                    flag=False
                elif chess[x + k][y + l]=='B':
                    flag = False
                elif l==7:
                    flag = True

            elif flag==False:
                if chess[x + k][y + l]!='W':
                    chess[x + k][y + l] = 'W'
                    cnt=cnt+1
                    flag=True
                elif chess[x + k][y + l]=='W':
                    flag = True
                elif l==7:
                    flag = False



#체스판 자르는거 -> 자르지말고 시작점 보내는 법 생각!!
for i in range(a-7):
    for j in range(b-7):
        checkNum(i,j)

