def preorder(n):
    if n:
        result.append(tree[n])
        preorder(a1[n])
        preorder(a2[n])

T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    a1 = [0] * (N + 1)
    a2 = [0] * (N + 1)

    for i in range(N):
        node, n, *a = input().split()
        node = int(node)
        if a:
            a = list(map(int, a))
            a1[node] = a[0]
            a2[node] = a[1]
        tree[node] = n

    result = []
    preorder(1)
    stack = []
    while result:
        x = result.pop()
        if x.isdigit():
            stack.append(int(x))
        else:
            j = stack.pop()
            k = stack.pop()
            if x == '+':
                stack.append(j+k)
            elif x == '-':
                stack.append(j-k)
            elif x == '/':
                stack.append(j//k)
            else:
                stack.append(j*k)
    print(f'#{tc} {stack[0]}')