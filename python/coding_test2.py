flag = True

def DFS(h, w, n, x, y, depth, board):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    depth = depth + 1
    visited[x][y] = 1
    if depth == n:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h or depth > n+2:
                continue
            elif board[nx][ny] == '1' and visited[nx][ny] == 0:
                return False
        return True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > w or ny < 0 or ny > h or depth > n+2:
            continue
        elif board[nx][ny] == '1' and visited[nx][ny] == 0:
            if DFS(h, w, n, nx, ny, depth, board) == True:
                continue

def solution(h, w, n, board):
    count=0
    depth = 0
    flag = True
    for a in range(h):
        for b in range(w):
            if board[a][b] == '1':
                if DFS(h, w, n, a, b, depth, board) == False:
                    flag = False
                    break

        if flag == True:
            count=count+1

    return count

print(solution(7,9,4,["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]))
# 10
print(solution(5,5,5,["11111","11111","11111","11111","11111"]))
# 12
