def node(n):
    if n <= N:
        if tree[n]:
            return tree[n]
        else:       #부모 노드의 값이 자식 노드 두 값의 합
            return node(2*n) + node(2*n +1)
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(1, M+1):
        n, m = map(int, input().split())
        tree[n] = m

    print(f'#{tc} {node(L)}')

