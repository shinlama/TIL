N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    j = lst[i][0]
    if i + j <= N:
        p = lst[j][1]
        dp[i] = max(dp[i+1], dp[i+j] + p)
    else:
        dp[i] = dp[i+1]

print(dp[0])
