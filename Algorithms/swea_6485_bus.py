T = int(input())

for tc in range(1, T+1):
    N = int(input())
    AB = {}
    for i in range(1, 5001):
        AB[i] = 0
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            AB[j] += 1

    P = int(input())
    result = []
    for i in range(P):
        result.append(AB[int(input())])

    print(f'#{tc}', *result)