T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N-1):
        for j in range(N-1):

            lst1 = []
            a = b = c = d = 0
            for p in range(N):
                for k in range(N):
                    if p <= i and k <= j:
                        a += arr[p][k]
                    elif p <= i and k > j:
                        b += arr[p][k]
                    elif p > i and k <= j:
                        c += arr[p][k]
                    else:
                        d += arr[p][k]
                    lst1 = [a,b,c,d]

            lst.append(lst1)

    minV = 1000000
    for l in lst:
        if max(l) - min(l) < minV:
            minV = max(l) - min(l)

    print(f'#{tc} {minV}')
