#도착했을 때
def f(i, j, n):
    if arr[i][j] ==3:
        return arr[i][j]-2
    else:
        arr[i][j] = 1       #중복방지
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]!=1:
                if f(ni, nj, n):
                    return cnt
        return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]

    #시작점 찾기
    sti = -1
    stj = -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                sti, stj = i, j
                break
    print(f'#{tc} {f(sti, stj, n)}')