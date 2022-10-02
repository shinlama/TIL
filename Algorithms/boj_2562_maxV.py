lst = list(int(input()) for _ in range(9))
maxV = max(lst)

for i in range(9):
    if maxV == lst[i]:
        ans = i
print(maxV)
print(ans+1)