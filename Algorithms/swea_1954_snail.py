T = int(input())

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    i, j = 0, 0
    snail_index = 0

    for k in range(1, N*N +1):
        snail[i][j] = k
        i += row[snail_index]
        j += col[snail_index]
        if i < 0 or j < 0 or i >= N or j >= N or snail[i][j]!=0:
            i -= row[snail_index]
            j -= col[snail_index]
            snail_index = (snail_index+1)%4
            i += row[snail_index]
            j += col[snail_index]

    print(f"#{tc}")
    for m in snail:
        print(*m)