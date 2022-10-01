T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    result = []
    for i in range(N-M+1):
        result.append(sum(lst[i:i+M]))

    ans = max(result) - min(result)


    print(f'#{tc} {ans}')