def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    l = [n for n in lst[1:] if n < pivot]
    r = [n for n in lst[1:] if n >= pivot]
    return quick_sort(l) + [pivot] + quick_sort(r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {quick_sort(lst)[N//2]}')

