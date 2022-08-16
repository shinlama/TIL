T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    arr2 = [[arr[i][j] for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                result = ''.join(arr[i][j:j+M])
            if arr2[i][j:j+M] == arr2[i][j:j+M][::-1]:
                result = ''.join(arr2[i][j:j+M])


    print(f'#{tc} {result}')