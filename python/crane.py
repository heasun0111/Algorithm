def solution(board, moves):
    basket=[]
    answer = 0
    N=len(board)
    for i in range(len(moves)):
        crane=moves[i]-1
        for j in range(N):
            if board[j][crane]!=0:
                doll=board[j][crane]
                board[j][crane]=0
                basket.append(doll)
                #바구니 속 인형 삭제
                if len(basket)>=2 and basket[-1]==basket[-2]:
                    del basket[-1]
                    del basket[-1]
                    answer=answer + 2
                break

            else:
                continue
    return answer


#print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))