T = int(input())

def find2():
    lst2 = []
    if arr[i][j] == 2:
        lst2.append((i,j))
    return lst2

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    find2()
    for i in range(N):
        for j in range(N):
            if 