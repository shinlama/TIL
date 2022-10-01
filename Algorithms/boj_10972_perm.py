from itertools import permutations

n = int(input())
find = tuple(map(int, input().split()))
lst = [i for i in range(1, n+1)]

comb_lst = list(permutations(lst, n))

for tu in range(len(comb_lst)):
    try:
        if comb_lst[tu] == find:
            print(*comb_lst[tu+1])
    except:
        print(-1)



