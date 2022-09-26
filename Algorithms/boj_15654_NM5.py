N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
def dfs():
    if len(arr) == M:
        print(*arr)
        return
    for i in lst:
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()
dfs()

