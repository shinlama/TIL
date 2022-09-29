T = int(input())
def find(x):
    while x != tree[x]:
        x = tree[x]
    return x

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [i for i in range(N+1)]

    for i in range(M):
        c1, c2 = lst[2 * i], lst[2*i+1]
        tree[find(c2)] = find(c1)

    ans = 0
    for num in range(1, N+1):
        if tree[num] == num:
            ans += 1

    print(f'#{tc} {ans}')