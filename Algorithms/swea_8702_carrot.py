T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    a = 0
    lst2 = []
    for i in range(N):
        a += lst[i]
        lst2.append(a)

    lst3 = []
    for j in range(N):
        lst3.append(sum(lst) - lst2[j])

    lst4 = []
    for k in range(N):
        lst4.append(abs(lst2[k]- lst3[k]))

    result = 0
    for p in range(N):
        if lst4[p] == min(lst4):
            result = p


    print(f'#{tc} {result+1} {min(lst4)}')