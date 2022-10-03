def double(n,m):
    ans = 1
    for i in range(m):
        ans *= n
    return ans

for tc in range(1, 11):
    t = int(input())
    N,M= map(int, input().split())

    print(f'#{tc} {double(N,M)}')
