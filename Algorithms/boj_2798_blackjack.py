N, M = map(int, input().split())
lst = list(map(int, input().split()))

my_max = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if lst[i] + lst[j] + lst[k] > M:
                continue
            elif my_max < lst[i] + lst[j] + lst[k]:
                my_max = lst[i] + lst[j] + lst[k]

print(my_max)