# 같은 칸에 파이어볼 합쳐지는거 어떻게 구현?
# 자료형, 표현 방식 -> 이름을 좌표, 요소를 불에 관한거!
# fireballs[(r-1, c-1)].append((m, s, d)) # fireballs[(r, c)] : [(m, s, d), (m, s, d)...]
# defaultdict 이용!

N, M, K = map(int, input().split())
board=[[0 for _ in range(N)] for _ in range(N)]


fireball=[]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r, c, m, s, d])

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

# 같은 칸에 파이어볼 합쳐지는거 어떻게 구현?
# 배열에 넣고 len( )>1인 좌표만 불꽃 합치기 실행
for _ in range(K):
    tmp_fireball=[]
    for FB in fireball:











'''
ri, ci, mi, si, di
1 1 5 2 2
1 4 7 1 6
'''