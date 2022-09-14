def inorder(a):
    if a <= N:
        inorder(a*2)
        print(lst[a], end='')
        inorder(a*2+1)

for tc in range(1,11):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(N):
        li = list(input().split())
        lst[i+1] = li[1]
    print(f'#{tc}', end=' ')
    inorder(1)
    print()