def binary_search(page,x):
    start = 1
    end = page

    count=0
    while start <= end:
        mid = (start + end)//2 # 중간위치
        if mid == x:
            return count
        elif mid <x:
            start= mid
            count+=1
        elif mid> x:
            end= mid
            count+=1

T = int(input())
for tc in range(1,T+1):
    page, A, B = list(map(int,input().split()))

    A_result = binary_search(page,A)
    B_result = binary_search(page,B)

    if A_result > B_result:
        result='B'
    elif A_result < B_result:
        result='A'
    else:
        result=0
    print(f'#{tc} {result}')
