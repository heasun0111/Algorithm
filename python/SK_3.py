def solution(width, height, diagonals):
    dp = [[0 for i in range(width + 1)] for j in range(height + 1)]

    dp[0][0]=0
    for l in range(1,height+1):
        dp[l][0] = 1
    for k in range(1,width+1):
        dp[0][k] = 1

    for m in range(height):
        for k in range(width):
            dp[m+1][k+1]=dp[m+1][k]+dp[m][k+1]

    answer=0
    for q in range(len(diagonals)):
        tmp=diagonals[q]
        X=tmp[0]
        Y=tmp[1]

        answer=answer+(dp[Y-1][X])*(dp[height-Y][width-(X-1)])
        answer=answer+(dp[Y][X-1])*(dp[height-(Y-1)][width-X])

    answer = answer%10000019
    return answer

print(solution(2, 2, [[1,1],[2,2]]))
print(solution(51, 37, [[17,19]]))

#dp=[[0 for i in range(width+1)] for j in range(height+1)]로 선언하면
#dp[y][x]인거 명심!!