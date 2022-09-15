def heap(n):
    global idx
    idx += 1
    tree[idx] = lst[n]
    a = idx #자식 인덱스
    b = a // 2 #부모 위치
    while b and tree[a] < tree[b]:
        tree[a], tree[b] = tree[b], tree[a] #자식, 부모 바꿔줌
        a = b
        b = a // 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] * (N+1)
    idx = 0
    for i in range(N):
        heap(i)

    last = N #마지막 노드 위치
    result = 0
    while last:
        last //= 2 #부모 위치
        result += tree[last] #부모들 더해주기

    print(f'#{tc} {result}')