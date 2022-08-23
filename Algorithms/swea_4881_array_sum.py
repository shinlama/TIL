def f(i, N):
    global minV
    if i == N:
        s= 0
        for k in range(N):
            s += arr[k][p[k]]
        if minV > s:
            minV = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    p= [i for i in range(n)]
    minV = 1000
    f(0, n)
    print(f'#{tc} {minV}')