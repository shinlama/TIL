T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    si = sj = N // 2
    cnt = 0
    for i in range(N):
        for j in range(N):
            if abs(si - i) + abs(sj - j) <= N // 2:
                cnt += arr[i][j]

    print(f'#{tc} {cnt}')