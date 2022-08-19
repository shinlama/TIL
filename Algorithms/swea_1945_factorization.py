T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [2, 3, 5, 7, 11]		#인수 리스트 생성
    result = []
    for i in lst:
        sum_a = 0
        while N % i ==0:		#인수 안 나누어떨어질 때까지 나누고 a,b,c,d,e값 찾기
            N = N / i
            sum_a += 1
        result.append(sum_a)	#a,b,c,d,e값 리스트에 넣기

    print(f'#{tc}', *result)
