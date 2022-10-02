T = 10
for t in range(1, T+1):
    tc = int(input())
    str = input()
    long_str = input()

    l = len(str)
    cnt = 0
    for i in range(len(long_str)-l+1):
        if str == long_str[i:i+l]:
            cnt += 1

    print(f'#{tc} {cnt}')