def f(i, k):
    global minV
    if i == k:
        s = 0
        for l in range(k):
            s += arr[l][lst[l]]
        if minV > s:
            minV = s
        #print(lst)
    else:
        for j in range(i, k):
            lst[i], lst[j] = lst[j], lst[i]
            f(i+1, k)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(N)]
    minV = 10*N
    f(0, N)
    print(f'#{tc} {minV}')