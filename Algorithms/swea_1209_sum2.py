import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row = []
    col = []
    cnt1 = cnt2 = 0
    ans = 0
    for n in range(100):
        cnt1 += arr[n][n]
        cnt2 += arr[n][99-n]

        n_sum = m_sum = 0
        for m in range(100):
            n_sum += arr[n][m]
            m_sum += arr[m][n]
        row.append(n_sum)
        col.append(m_sum)
    cnt3 = max(row)
    cnt4 = max(col)

    print(f'#{tc} {max(cnt1, cnt2, cnt3, cnt4)}')