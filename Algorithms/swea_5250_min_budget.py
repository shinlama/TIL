T = int(input())

def bfs(i, j):
    visited[i][j] = 0
    queue = []
    queue.append((i, j))
    while queue:
        si, sj = queue.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N:
                tmp = 0
                if arr[ni][nj] > arr[si][sj]:
                    tmp = arr[ni][nj] - arr[si][sj]
                if visited[si][sj] + tmp + 1 < visited[ni][nj]:
                    visited[ni][nj] = visited[si][sj] + tmp + 1
                    queue.append((ni,nj))
    return visited[N-1][N-1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]

    print(f'#{tc} {bfs(0,0)}')