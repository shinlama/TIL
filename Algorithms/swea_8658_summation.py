T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())

    sum = []
    for i in lst:
        s = 0
        for j in i:
            s += int(j)
        sum.append(s)

    print(f'#{tc} {max(sum)} {min(sum)}')