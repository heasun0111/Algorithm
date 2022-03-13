from itertools import combinations

def solution(cards):
    answer = 0
    hashing=[[0 for i in range(10)] for j in range(4)]
    #카드 해싱
    for str in cards:
        if str[0]=='S':
            num=int(str[1])
            hashing[0][num]=1
        elif str[0]=='C':
            num=int(str[1])
            hashing[1][num]=1
        elif str[0]=='D':
            num=int(str[1])
            hashing[2][num]=1
        elif str[0]=='H':
            num=int(str[1])
            hashing[3][num]=1

    #모양 같은거
        for i in range(4):
            number=0
            for j in range(10):
                if hashing[i][j]==1:
                    number=number+1
            if number>=3:



    print(hashing)
    return answer


print(solution(["C8","H8","C7","C0","D8","S8"]))