t = int(input())
for tc in range(t):
    lst = list(input())

    cnt = tmp = 0
    for i in range(len(lst)):
        if lst[i] =='O':
            tmp += 1
            cnt += tmp
        else:
            tmp = 0
    print(cnt)