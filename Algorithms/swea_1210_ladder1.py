import sys
sys.stdin = open("input.txt", "r")
for _ in range(1,11):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    for col in range(100):
        if arr[99][col]==2:
            break

    row = 99
    while row > 0:
        if col>0 and arr[row][col-1]==1:
            arr[row][col] = -1
            col -= 1
        elif col<99 and arr[row][col+1]==1:
            arr[row][col] = -1
            col += 1
        else:
            row -= 1
    print(f"#{tc} {col}")