#도착했을 때
def f(i, j):
    if arr[i][j] ==3:
        return 1
    else:
        arr[i][j] = 1       #중복방지
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj]!=1:
                if f(ni, nj):
                    return 1
        return 0

T = 10
for t in range(1, T+1):
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(16)]

    #시작점 찾기
    sti = -1
    stj = -1
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                sti, stj = i, j
                break
    print(f'#{tc} {f(sti, stj)}')