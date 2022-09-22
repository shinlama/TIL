dx = [0, 1]
dy = [1, 0]

def min_sum(x, y, my_sum):
    global minn
    if x == N-1 and y == N-1:
        if my_sum < minn:
            minn = my_sum
    if my_sum > minn:
        return
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < N and ny < N:
                min_sum(nx, ny, my_sum + arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minn = int(1e9)
    min_sum(0, 0, arr[0][0])
    print(f'#{tc} {minn}')