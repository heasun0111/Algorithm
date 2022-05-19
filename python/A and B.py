# S에서 T로 변환가능한지 확인이 아니라, T에서 S로 변환 가능한지 확인!!
S=input()
T=input()
numT=len(T)-1
numS=len(S)-1

for i in range(numT, numS, -1):
    #슬라이싱 이용
    if T[i]=='A':
        #T.rstrip('A')
        T=T[:-1]

    elif T[i]=='B':
        T=T[:-1]
        T=T[::-1]

if T==S:
    print(1)
else:
    print(0)