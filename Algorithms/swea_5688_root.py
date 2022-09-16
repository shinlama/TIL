T = int(input())

for tc in range(1, T+1):
    n = int(input())
    m = round(n**(1/3))
    result = m
    if m ** 3 != n:
        result = -1

    print(f'#{tc} {result}')