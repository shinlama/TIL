T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())), reverse=True)

    ans = 0
    for i in range(K):
        ans += lst[i]

    print(f'#{tc} {ans}')