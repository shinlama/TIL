T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    #cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(1, N):
                if arr[i][j:j+k] == '#'*k:
                    cnt += 1

    print(arr, cnt)