def f(a):
    if a == 1:		#첫째 값 설정
        result = 1
    elif a == 2:		#둘째 값 설정
        result = 3
    elif a >= 3:		#점화식
        result = f(a-1) + 2 * f(a-2)
    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input()) // 10

    print(f'#{tc} {f(n)}')