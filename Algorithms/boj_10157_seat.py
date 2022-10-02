C, R = map(int, input().split())
num = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[0] * C for _ in range(R)]

if num > C*R:
    print(0)
else:
    i, j, dr = 0, R, 0
    for cnt in range(1, C*R +1):
        arr[i][j] = cnt
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dr = (dr+1) % 4
            i = i+ di[dr]
            j = j+ dj[dr]

    arr = list(zip(arr[::-1]))
    arr2 = []
    for lst in arr:
        arr2.append(lst[0])

    for n in range(R):
        for m in range(C):
            if num == arr2[n][m]:
                a = R-n
                b = C-m

    print(a, b)
