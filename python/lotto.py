
def combi(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], r-1):
                yield [arr[i]]+next


# 띄어쓰기로 구분된 문자 -> 리스트
K=list(input().split())

# input을 아예 문자열로 받아옴!
while K[0]!='0':
    arr=K[1:]
    for tmp in combi(arr, 6):
        ans=" ".join(tmp)
        print(ans)
    print(' ')
    K=list(input().split())

# EOFError 런타임 에러 -> End Of File Error인데
# 나는 적절한 때 파일이 종료되지 않아서 생기는 것 같음
