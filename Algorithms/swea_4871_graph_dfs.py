def dfs(v):
    visited[v] = True       #visited[v]를 True로 설정
    move.append(v)
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(1, E+1):
        a, b = map(int, input().split())
        arr[a].append(b)       #빈 배열에 a,b값 넣기

    move = []
    S, G = map(int,input().split())
    dfs(S)
    result = 1
    if G not in move:       #dfs 돌렸을 때 G 없으면 0
        result = 0

    print(f'#{tc} {result}')

