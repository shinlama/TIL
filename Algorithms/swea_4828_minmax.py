T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {max(lst)-min(lst)}')