T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 빈 행렬 만들어줌
    arr = [[''] * 10 for _ in range(10)]
    # 만 행렬에 color 1이면 red, 2이면 blue 추가
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if color == 1:
                    arr[i][j] += 'red'
                else:
                    arr[i][j] += 'blue'

    count = 0
    for i in range(10):
        for j in range(10):
            if ('red' in arr[i][j]) and ('blue' in arr[i][j]):
                count += 1

    print(f'#{tc} {count}')