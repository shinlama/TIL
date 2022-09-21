def swap(prize, i, j):
    prize_arr = [0] * cnt
    for k in range(cnt-1, -1, -1):
        prize_arr[k] = prize % 10
        prize //= 10
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]
    prize = 0
    for k in range(cnt):
        prize = prize * 10 + prize_arr[k]
    return prize

def find(n, k, prize):
    global ans
    for i in range(720):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return
    if n == k:
        if prize > ans:
            ans = prize
    else:
        for i in range(cnt-1):
            for j in range(i+1, cnt):
                find(n, k+1, swap(prize, i, j))

T = int(input())
for tc in range(1, T+1):
    prize, N = map(int, input().split())
    memo = [[0] * 720 for _ in range(N+1)]
    tmp = prize
    # 입력된 숫자판다(prize)의 길이를 구해본다.
    cnt = 0
    while tmp:
        tmp //= 10
        cnt += 1

    ans = 0
    find(N, 0, prize)
    print(f'#{tc} {ans}')