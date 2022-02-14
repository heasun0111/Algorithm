def solution(clothes):
    dict={}
    ans=1
    for list in clothes:
        key=list[1]
        value=list[0]
        if key in dict:
            dict[key].append(value)
        else:
            dict[key]=[value]

    for key in dict.keys():
        ans = ans*(len(dict[key])+1)

    return ans-1

#print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))