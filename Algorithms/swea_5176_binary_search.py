def inorder(n):
    global idx
    if n <= N:
        inorder(2 * n)
        tree[n] = num[idx]
        idx += 1
        inorder(2 * n + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    num = list(range(1, N+1))
    idx = 0
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')