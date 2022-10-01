import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    j_lst = []
    for j in range(100):
        if arr[0][j] == 1:
            j_lst.append(j)

    cnt_lst = []
    for j in j_lst:
        cnt = 0
        i = 0
        while i < 99:
            if j > 0 and arr[i][j-1] == 1:
                arr[i][j] = -1
                j -= 1
            elif j < 99 and arr[i][j+1] == 1:
                arr[i][j] = -1
                j += 1
            else:
                i += 1
            cnt += 1
        cnt_lst.append(cnt)

    print(f'#{tc} {j_lst[cnt_lst.index(min(cnt_lst))]}')