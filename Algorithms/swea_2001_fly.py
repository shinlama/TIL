T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = N-M+1

    my_max = 0
    for i in range(a):
        for j in range(a):
            my_sum = 0
            for k in range(M):
                for l in range(M):
                    my_sum += arr[i+k][j+l]
            if my_sum > my_max:
                my_max = my_sum

    print(f'#{tc} {my_max}')