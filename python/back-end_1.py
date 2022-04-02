def solution(dist):
    N=len(dist)
    answer = []
    tmp1 = []

    max=-1
    max_x = -1
    max_y = -1

    for i in range(N):
        for j in range(N):
            if dist[i][j]>max:
                max=dist[i][j]
                max_x = j
                max_y = i

    if max_x < max_y:
        tmp1.append(max_x)

    elif max_x > max_y:
        tmp1.append(max_y)

    tmp=[]
    for k in range(N):
        if k!=max_y and k!=max_x:
            tmp.append([dist[max_y][k], k])

    tmp.sort(key=lambda x: x[0])

    for l in range(N-2):
        tmp1.append(tmp[l][1])

    if max_x < max_y:
        tmp1.append(max_y)

    elif max_x > max_y:
        tmp1.append(max_x)

    tmp2=[]
    for m in range(len(tmp1)):
        tmp2.append(tmp1[m])

    tmp2.reverse()
    answer.append(tmp1)
    answer.append(tmp2)

    return answer

print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))
print(solution([[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]))