def solution(bridge_length, weight, truck_weights):
    cnt = 0
    sum_bridge=0
    bridge=[0 for i in range(bridge_length-1)]
    bridge.append(truck_weights[0])
    sum_bridge=sum_bridge+truck_weights[0]
    cnt=cnt+1

    idx = 1
    while(idx!=len(truck_weights)):
        sum_bridge=sum_bridge-bridge[0]
        bridge.pop(0)
        if idx<len(truck_weights) and sum_bridge+truck_weights[idx]<=weight:
            sum_bridge=sum_bridge+truck_weights[idx]
            bridge.append(truck_weights[idx])
            idx=idx+1
            cnt=cnt+1
        else:
            bridge.append(0)
            cnt = cnt + 1
    answer = cnt + bridge_length
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

#sum은 시간 복잡도 O(n)이다!