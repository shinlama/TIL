T = int(input())
for x in range(1, T+1):
    N = int(input())
    a = list(map(int,input().split()))
    max = a[0]
    min = a[0]
    for num in a :
        if max < num :
            max = num
        if num < min :
            min = num
    result = max - min
    print(f'#{x} {result}')