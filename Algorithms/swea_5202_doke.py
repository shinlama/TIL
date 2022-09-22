T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 인덱스[1] 값 기준으로 정렬하기, 같으면 인덱스[0] 값 오름차순
    arr2 = sorted(arr, key=lambda x: (x[1], x[0]))

    c = 0
    result = 0
    for i in range(N):
        if arr2[i][0] >= c:
            c = arr2[i][1]
            result += 1

    print(f'#{tc} {result}')