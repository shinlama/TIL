T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())))

    for i in range(N):
        try:
            if lst[i] // M * K >= i+1:
                ans = 'Possible'
            else:
                ans = 'Impossible'
        except:
            ans = 'Impossible'

    print(f'#{tc} {ans}')