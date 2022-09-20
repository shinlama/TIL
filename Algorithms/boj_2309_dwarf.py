def dwarf(lst):
    for j in range(8):
        for k in range(j + 1, 9):
            if lst[j] + lst[k] == who:
                lst.pop(j)
                lst.pop(k - 1)
                return lst

lst = []
for i in range(1, 10):
    n = int(input())
    lst.append(n)
    lst.sort()

who = sum(lst) - 100
lst2 = dwarf(lst)

for i in lst2:
    print(i)