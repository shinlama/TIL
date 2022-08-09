T = int(input())
for x in range(T):
    cnt = [0 for x in range(10)]
    tmp = [0 for x in range(2)]
    n = int(input())
    a = list(map(int,input()))

    for num in a :
        cnt[num] += 1
    maxNum = 0
    for idx, c in enumerate(cnt):
        if c >= maxNum:
            maxNum = c
            tmp[0] = idx
            tmp[1] = c
    print(f'#{(x+1)} {tmp[0]} {tmp[1]}')