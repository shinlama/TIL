T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int,input().split()))
    charge = list(map(int,input().split()))
    count = 0
    current = 0

    while current + K < N :
        for step in range(K, 0, -1):
            if (current + step) in charge:
                current += step
                count += 1
                break
        else:
            count = 0
            break
    print(f'#{tc} {count}')
