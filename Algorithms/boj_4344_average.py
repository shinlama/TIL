c = int(input())
for tc in range(c):
    N, *lst = map(int, input().split())

    aver = sum(lst) / N

    cnt = 0
    for i in lst:
        if i > aver:
            cnt += 1

    print('{:.3f}%'.format(cnt/N * 100))