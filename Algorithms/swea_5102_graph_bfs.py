def bfs(start, end):
    visited = [-1]*(V+1)
    que = []
    que.append((start,end))
    visited[start] = 0

    while que:
        w, v = que.pop(0)
        if w == v:
            return visited[v]
        for i in arr[w]:
            if visited[i] == -1:
                que.append((i,v))
                visited[i] = visited[w] +1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(1, E+1):
        a, b = map(int, input().split())
        arr[a].append(b)       #빈 배열에 a,b값 넣기
        arr[b].append(a)

    S, G = map(int,input().split())
    print(f'#{tc} {bfs(S, G)}')