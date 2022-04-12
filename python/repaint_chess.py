#파이썬 입력도 공부하자!!
a, b = map(int, input().strip().split(' '))
chess=[]
answer=[]

for _ in range(a):
    chess.append(input())

# % 이용해서 flag 없이 구현 가능
# chess[x+k][y+l] 좌표에서 x+k와 y+l 주의!!
def checkNum_B(x,y):
    cnt=0
    for k in range(8):
        for l in range(8):
            if ((x+k)+(y+l))%2==0:
                if chess[x+k][y+l]!='B':
                    cnt=cnt+1
            elif ((x+k)+(y+l))%2==1:
                if chess[x+k][y+l]!='W':
                    cnt=cnt+1
    return cnt

def checkNum_W(x,y):
    cnt=0
    for k in range(8):
        for l in range(8):
            if ((x+k)+(y+l))%2==0:
                if chess[x+k][y+l]!='W':
                    cnt=cnt+1
            elif ((x+k)+(y+l))%2==1:
                if chess[x+k][y+l]!='B':
                    cnt=cnt+1
    return cnt


#체스판 자르는거 -> 자르지말고 시작점 보내는 법 생각!!
for i in range(a-7):
    for j in range(b-7):
        answer.append(checkNum_B(i,j))
        answer.append(checkNum_W(i,j))

print(min(answer))
