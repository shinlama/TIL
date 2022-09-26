T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())

        for i in range(A, B+1):
            lst[i] += 1

    result = []
    P = int(input())
    for j in range(P):
        a = int(input())
        result.append(lst[a])

    print(f'#{tc}', *result)