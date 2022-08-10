T= int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    answer += abs(arr[i][j] - arr[nx][ny])
    print(f"#{tc} {answer}")