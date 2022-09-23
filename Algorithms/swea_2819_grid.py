T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(num, x, y):
    if len(num) == 7:
        lst.append(num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(arr[nx][ny] + num, nx, ny)
    return

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    lst = []
    for i in range(4):
        for j in range(4):
            dfs('', i, j)

    my_set = set(lst)

    print(f'#{tc} {len(my_set)}')