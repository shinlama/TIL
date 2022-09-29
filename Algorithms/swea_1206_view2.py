import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    for i in range(2, N-2):
        if lst[i] > lst[i-2] and lst[i] > lst[i-1] and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            ans += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])

    print(f'#{tc} {ans}')