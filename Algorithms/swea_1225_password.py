T = 10
for t in range(1, T+1):
    tc = int(input())
    lst = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        t = lst.pop(0) - i
        if t <= 0:
            lst.append(0)
            break
        lst.append(t)
        i += 1

    print(f'#{tc}', *lst)