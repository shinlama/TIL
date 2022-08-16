T = int(input())

for tc in range(1, T+1):
    n = list(map(str,input()))
    m = list(map(str,input()))

    result = []
    for i in n:
        cnt = 0
        for j in m:
            if i == j:
                cnt += 1
        result.append(cnt)

    max_cnt = 0
    for j in result:
        if j > max_cnt:
            max_cnt = j


    print(f'#{tc} {max_cnt}')