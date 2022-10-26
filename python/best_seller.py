# 딕셔너리 key정렬, value정렬

book={
}

N=int(input())

for _ in range(N):
    tmp=input()
    if tmp not in book:
        book[tmp]=1

    else:
        book[tmp]=book[tmp]+1

ans=dict(sorted(book.items(), reverse=True))
answer=dict(sorted(ans.items(), key=lambda x:x[1]))

answer2=list(answer.keys())
# .keys()는 배열이 아니라서 list()로 감싸야 한다.
print(answer2[-1])

