import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        if arr[99][j] == 2:
            break

    i = 99
    while i > 0:
        if j < 99 and arr[i][j+1] == 1:
            arr[i][j] = -1
            j += 1
        elif j > 0 and arr[i][j-1] == 1:
            arr[i][j] = -1
            j -= 1
        else:
            i -= 1

    print(f'#{tc} {j}')