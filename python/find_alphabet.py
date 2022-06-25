
S=input()

alphabet=[ '-1' for _ in range(26)]

for i in range(len(S)):
    # S에서는 소문자만 들어간다!! -> num이 범위를 넘어갈 뻔 함
    num=ord(S[i])-97

    if alphabet[num]=='-1':
        alphabet[num]=str(i)
    else:
        continue

answer=" ".join(alphabet)

print(answer)