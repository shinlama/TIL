T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A_list = list(range(1,13))

    count = 0
    for i in range(1<<len(A_list)):
        sum = 0
        lenn = 0
        for j in range(len(A_list)):
            if i & (1<<j):
                sum += A_list[j]
                lenn += 1
        if lenn == N and sum == K:
            count += 1
    print(f'#{tc} {count}')