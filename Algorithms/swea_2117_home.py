cost = [K ** 2 * 2 - 2 * K + 1 for K in range(41)]
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i,j))

    result = 0
    for si in range(N):
        for sj in range(N):
            cnts = [0] * 41
            for i, j in home:
                d = abs(si - i) + abs(sj - j) + 1
                cnts[d] += 1

            cnt = 0
            for k in range(1,41):
                cnt += cnts[k]
                if cnt*M >= cost[k] and result < cnt:
                    result = cnt
 
    print(f'#{tc} {result}')