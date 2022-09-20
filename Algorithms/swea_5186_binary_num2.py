T = int(input())

for tc in range(1, T+1):
    n = float(input())
    num = ''
    t = 1
    while True:
        m = n // (0.5)**t
        if m == 1:
            num += '1'
            n = n - (0.5)**t
        else:
            num += '0'
        if t > 12:
            num = 'overflow'
        if n == 0:
            break
        t += 1

    print(f'#{tc} {num}')
