T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())

    idx = 0
    cnt = 0
    for i in range(len(A)-len(B)+1):
        if A[idx:idx+len(B)] == B:
            cnt += 1
            idx = idx + len(B) - 1
        idx += 1

    result = len(A) - ((len(B)-1) * cnt)

    print(f'#{tc} {result}')