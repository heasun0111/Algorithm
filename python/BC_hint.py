dir = [
    [0, 0],
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0]
]

T = int(input())

for tc in range(1, T + 1):
    M, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AP = []
    ans = 0
    for _ in range(P):
        AP.append(list(map(int, input().split())))
    A.insert(0, 0)
    B.insert(0, 0)
    ax, ay = 1, 1
    bx, by = 10, 10

    for m in range(M + 1):
        ax, ay = dir[A[m]][0] + ax, dir[A[m]][1] + ay
        bx, by = dir[B[m]][0] + bx, dir[B[m]][1] + by

        AC = []
        BC = []
        for bc in AP:
            diff_a, diff_b = abs(bc[0] - ax) + abs(bc[1] - ay), abs(bc[0] - bx) + abs(bc[1] - by)
            if diff_a <= bc[2]: AC.append(bc)
            if diff_b <= bc[2]: BC.append(bc)

        if not AC and BC:
            temp = 0
            for bc in BC:
                temp = max(temp, bc[3])
            ans += temp
        elif AC and not BC:
            temp = 0
            for ac in AC:
                temp = max(temp, ac[3])
            ans += temp
        elif AC and BC:
            temp = 0
            #완전 탐색으로 확인
            for ac in AC:
                for bc in BC:
                    if ac == bc:
                        temp = max(temp, ac[3])
                    else:
                        temp = max(temp, ac[3] + bc[3])
            ans += temp
    print(f'#{tc} {ans}')