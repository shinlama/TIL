T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0
    length = 0
    for i in range(len(A)-len(B)+1):
        if A[cnt:cnt+len(B)] == B:
            length += 1
            cnt = cnt + len(B) - 1
        cnt += 1

    result = len(A) - ((len(B)-1) * length)

    print(f'#{tc} {result}')