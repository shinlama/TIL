for _ in range(10):
    tc = int(input())
    # 100*100
    lst = [list(map(int, input().split())) for _ in range(100)]

    result = []

    for y in range(len(lst)):
        sum1 = 0
        for x in range(len(lst)):
            sum1 += lst[y][x]
        result.append(sum1)

    for x in range(len(lst)):
        sum2 = 0
        for y in range(len(lst)):
            sum2 += lst[y][x]
        result.append(sum2)

    sum3 = 0
    for y in range(len(lst)):
        for x in range(len(lst)):
            if y == x:
                sum3 += lst[y][x]
    result.append(sum3)

    sum4 = 0
    for y in range(len(lst)):
        for x in range(len(lst)):
            if y == len(lst)-x:
                sum4 += lst[y][x]
    result.append(sum4)

    my_max = 0
    for i in result:
        if i > my_max:
            my_max = i

    print(f'#{tc} {my_max}')