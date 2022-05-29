#시간초과

def ShiftRow(board):
    tmp=board.pop()
    board.insert(0,tmp)
    return board

def Rotate(board):
    column=len(board)
    row=len(board[0])
    queries = [[1, 1, column, row]]

    if row>column:
        arr_tmp=[[0] * row for _ in range(row)]
    else:
        arr_tmp=[[0]*column for _ in range(column)]

    for i in range(column):
        for j in range(row):
            if board[i][j]!=0:
                arr_tmp[i][j]=board[i][j]

    for t, l, b, r in queries:
        top, left, bottom, right = t - 1, l - 1, b - 1, r - 1
        temp = arr_tmp[top][left]
        for k in range(top, bottom):
            arr_tmp[k][left] = arr_tmp[k + 1][left]
        for k in range(left, right):
            arr_tmp[bottom][k] = arr_tmp[bottom][k + 1]
        for k in range(bottom, top, -1):
            arr_tmp[k][right] = arr_tmp[k - 1][right]
        for k in range(right, left, -1):
            arr_tmp[top][k] = arr_tmp[top][k - 1]
        arr_tmp[top][left + 1] = temp

    arr_ans=[]
    for n in range(len(arr_tmp)):
        arr_ans_tmp = []
        for m in range(len(arr_tmp)):
            if arr_tmp[n][m]!=0:
                arr_ans_tmp.append(arr_tmp[n][m])
        if len(arr_ans_tmp)!=0:
            arr_ans.append(arr_ans_tmp)
    return arr_ans

def solution(rc, operations):
    for str in operations:
        if str=="ShiftRow":
            rc=ShiftRow(rc)
        elif str=="Rotate":
            rc=Rotate(rc)
    return rc


#print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate"]))
#print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["ShiftRow"]))
#print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow"]))
#print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print("구분")
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))