def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    g1 = lst[:mid]
    g2 = lst[mid:]

    merge_sort(g1)
    merge_sort(g2)

    if g1[-1] > g2[-1]:
        cnt += 1

    l = r = 0
    idx = 0
    while l < len(g1) and r < len(g2):
        if g1[l] < g2[r]:
            lst[idx] = g1[l]
            l += 1
            idx += 1
        else:
            lst[idx] = g2[r]
            r += 1
            idx += 1

    while l < len(g1):
        lst[idx] = g1[l]
        l += 1
        idx += 1

    while r < len(g2):
        lst[idx] = g2[r]
        r += 1
        idx += 1

    return lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    unsorted = list(map(int, input().split()))

    cnt = 0
    merge_sort(unsorted)

    print(f'#{tc} {unsorted[N//2]} {cnt}')