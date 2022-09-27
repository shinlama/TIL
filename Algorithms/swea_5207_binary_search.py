def search(lst, n, target):
    start = 0
    end = n - 1
    way = 0
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            if way == 2:
                break
            start = mid + 1
            way = 2
        else:
            if way == 1:
                break
            end = mid - 1
            way = 1
    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in B:
        if search(A, N, i):
            cnt += 1

    print(f'#{tc} {cnt}')