M, N = map(int, input().split())
t = int(input())
a_lst = []
b_lst = []
for _ in range(t):
    i, j = map(int, input().split())
    if i == 0:
        a_lst.append(j)
    else:
        b_lst.append(j)
a_lst.sort()
b_lst.sort()
a_lst.insert(0,0)
a_lst.append(N)
b_lst.insert(0,0)
b_lst.append(M)

ans_lst = []
for m in range(len(a_lst) -1):
    for n in range(len(b_lst) -1):
        ans_lst.append((a_lst[m+1] - a_lst[m]) * (b_lst[n+1] - b_lst[n]))

print(max(ans_lst))