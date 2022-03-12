def solution(money, costs):
    UseCost=[]
    UseCost.append(costs[0])
    for i in range(0,5):
        if i%2==1:
            if costs[i]*2 < costs[i+1]:
                UseCost.append(0)
            else:
                UseCost.append(costs[i+1])

        elif i%2==0:
            if costs[i]*5 < costs[i+1]:
                UseCost.append(0)
            else:
                UseCost.append(costs[i+1])
    answer = 0
    coin=[500,100,50,10,5,1]
    for j in range(6):
        if UseCost[5-j]!=0:
            answer=answer+(int((money/coin[j]))*UseCost[5-j])
            money=money%coin[j]

    return answer

#print(solution(4578, [1, 4, 99, 35, 50, 1000]))
#print(solution(1999, [2, 11, 20, 100, 200, 600]))