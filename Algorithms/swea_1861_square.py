dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(start):
    global N
    cnt = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        cnt += 1
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < N and 0 <=ny < N:
                if arr[x][y] +1 == arr[nx][ny]:
                    stack.append((nx,ny))
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [0, 0]

    for i in range(N):
        for j in range(N):
            cnt = search((i, j))
            if cnt > result[1]:
                result[1] = cnt
                result[0] = arr[i][j]
            elif cnt == result[1]:
                if arr[i][j] < result[0]:
                    result[0] = arr[i][j]

    print(f'#{tc} {result[0]} {result[1]}')