T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    result = []
    for i in range(n):
        my_lst = []
        for j in range(i + 1):
            if j == 0 or j == i:  # 양 끝에 1 배치
                my_lst.append(1)
            else:  # 윗 행의 숫자와 왼쪽 숫자의 합
                my_lst.append(result[i - 1][j] + result[i - 1][j - 1])
        result.append(my_lst)

    print(f'#{tc}')

    for i in result:
        print(*i)  # 인자의 출력