N, M = map(int, input().split())

lst = []
def dfs():
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()

dfs()