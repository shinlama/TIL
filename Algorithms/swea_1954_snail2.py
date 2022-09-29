di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    #초기값 설정
    i, j, dr = 0, 0, 0
    #cnt 1~n*n
    for cnt in range(1, n*n +1):
        arr[i][j] = cnt
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            #범위 체크가 먼저 와야한다. 인덱스 에러 방지
            i, j = ni, nj
        else:
            dr = (dr+1) % 4
            i = i+ di[dr]
            j = j+ dj[dr]

    print(f'#{tc}')
    for lst in arr:
        print(*lst)