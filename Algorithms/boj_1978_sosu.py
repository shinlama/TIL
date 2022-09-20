T = int(input())
arr = map(int, input().split())
result = 0
for i in arr:
    lst = []
    for j in range(1, i+1):
        if i % j == 0:
            lst.append(j)
    if len(lst) == 2:
        result += 1

print(result)