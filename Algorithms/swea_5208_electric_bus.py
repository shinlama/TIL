def f(i, N, c, e):
    global minV

    if e < 0:
        return
    elif i == N:
        if minV > c:
            minV = c
    elif c >= minV:
        return
    else:
        f(i+1, N, c+1, bus[i] - 1)
        if e > 0:
            f(i+1, N, c, e - 1)


T = int(input())
for tc in range(1, T+1):
    bus = list(map(int, input().split()))
    minV = bus[0]

    f(2, bus[0], 0, bus[1] - 1)
    print(f'#{tc} {minV}')