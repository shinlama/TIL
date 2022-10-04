T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    cnt1 = 0
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1] =='o':
                cnt += 1
            elif arr[j][i] == arr[j+1][i] == 'o':
                cnt1 += 1
    cnt2 = cnt3 = 0
    for m in range(N):
        if arr[m][m] == 'o':
            cnt2 += 1
        elif arr[m][N-m-1] == 'o':
            cnt3 += 1

    if cnt >= N-1 or cnt1 >= N-1 or cnt2 >= N-1 or cnt3 >= N-1:
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{tc} {ans}')