import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))


    for i in range(dump):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1

    print(f'#{tc} {max(lst) - min(lst)}')