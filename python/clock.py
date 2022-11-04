n=int(input())
board = [[0 for i in range(n)] for j in range(n)]

row=0
col=0

for i in range(7):
    cnt=0
    board[row+cnt][col]=i+1+cnt
    board[n-row][col+cnt]=i+1+cnt
    board[row][n-col-cnt]=i+1+cnt
    board[n-row-cnt][n-col]=i+1+cnt
    cnt=cnt+1

#while(0 not in l for l in board):


print(board)