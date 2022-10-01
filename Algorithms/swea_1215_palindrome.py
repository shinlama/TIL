T = 10
for tc in range(1, T+1):
    l = int(input())
    arr = [list(input()) for _ in range(8)]
    arr2 = list(zip(*arr[::-1]))

    cnt = 0
    for i in range(8):
        for j in range(8-l+1):
            word = arr[i][j:j+l]
            if word == word[::-1]:
                cnt += 1
            word2 = arr2[i][j:j+l]
            if word2 == word2[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')