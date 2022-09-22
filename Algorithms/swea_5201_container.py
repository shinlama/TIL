T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    W = sorted(list(map(int,input().split())))
    T = sorted(list(map(int,input().split())))

    result = 0
    for i in range(N-1, -1, -1):
        if len(T) == 0:
            break
        if T[-1] >= W[i]:
            result += W[i]
            T.pop(-1)
        elif T[-1] < W[i]:
            W.pop(-1)

    print(f'#{tc} {result}')