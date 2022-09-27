def permutation(lst, N):
    result = []
    if N == 0:
        return [[]]
    for i in range(len(lst)):
        elem = lst[i]
        for rest in permutation(lst[:i] + lst[i+1:], N-1):
            result.append([elem] + rest)
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    N_lst = [n for n in range(1, N+1)]
    per_lst = permutation(N_lst, N)

    cnt_lst = []
    for i in range(len(per_lst)):
        sum = 0
        for j in range(N):
            sum += arr[j][per_lst[i][j]-1]
        cnt_lst.append(sum)

    print(f'#{tc} {min(cnt_lst)}')
