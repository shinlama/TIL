T = int(input())
lst = list(map(int, input().split()))
lst.sort()
if T == 1:
    print(lst[0] ** 2)
else:
    print(lst[-1] * lst[0])
