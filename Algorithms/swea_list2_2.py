T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    cnt=0
    result=0
    for i in range(1 << len(arr)):
        sum = 0
        for j in range(len(arr)):
            if i & (1<<j):
                sum += arr[j]
                if sum == 0:
                    result = 1
                    break

    print(f"#{tc} {result}")