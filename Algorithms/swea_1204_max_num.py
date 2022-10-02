T = int(input())
for t in range(1, T+1):
    tc = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    maxV = 0
    cnt = 0
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            cnt += 1
    if maxV < cnt:
        maxV = cnt

    print(max)
