T = int(input())

for tc in range(1,T+1):
    n = str(input())
    m = str(input())

    result = 0
    for i in range(len(m)):
        if m[i:i+len(n)] == n:
            result = 1

    print(f'#{tc} {result}')