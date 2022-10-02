N = int(input())
lst = list(map(int, input().split()))

M = max(lst)
A = []
for i in lst:
    a = float(i/M) * 100
    A.append(a)

print(sum(A)/N)
