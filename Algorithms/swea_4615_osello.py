B, W = 1, 2
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [[0] * (N + 1) for _ in range(N + 1)]
    mid = N // 2
    board[mid][mid] = W
    board[mid + 1][mid + 1] = W
    board[mid+1][mid] = B
    board[mid][mid + 1] = B
 
    for _ in range(M):
        c, r, dol = map(int, input().split())
        board[r][c] = dol
 
        for i in range(8):
            for j in range(1, N):
                nr, nc = r + dr[i]*j, c + dc[i]*j
                if nr < 1 or nr > N or nc < 1 or nc > N or board[nr][nc] == 0:
                    break
                if board[nr][nc] == dol:
                    while nr != r or nc != c:
                        board[nr][nc] = dol
                        nr = nr - dr[i]
                        nc = nc - dc[i]
                    break
 
    bcnt = 0
    wcnt = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if board[r][c] == B: 
                bcnt += 1
            elif board[r][c] == W: 
                wcnt += 1
    print(f'#{tc}', bcnt, wcnt)
