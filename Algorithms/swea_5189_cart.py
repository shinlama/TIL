def battery(cnt, x, my_sum):
    global result
    if cnt == N:
        my_sum += arr[x][0]
        if my_sum < result:
            result = my_sum
            return
    if my_sum > result:
        return
    for i in range(1, N):
        if not arr[x][i]:
            continue
        if not visited[i]:
            visited[i] = 1
            battery(cnt + 1, i, arr[x][i] + my_sum)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 100 * N
    battery(1, 0, 0)

    print(f"#{tc} {result}")