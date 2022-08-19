for _ in range(10):
   tc, V = map(int, input().split())
   lst = list(map(int, input().split()))

   arr = {}
   for i in range(0, V*2, 2):
       j = lst[i]
       k= lst[i+1]
       arr[j] = arr.get(j, []) + [k]

   stack = []
   stack.append(0)
   graph = [0] * 100
   # 그래프 경로 저장
   while stack:
       x = stack.pop()
       graph[x] = 1
       if x in arr.keys():
           for y in arr[x]:
               if not graph[y]:
                   stack.append(y)

   print(f'#{tc} {graph[-1]}')