for tc in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))      # arr2는 arr1의 전치행렬

    result = ''
    cnt = 0
    while cnt < 100:        #가로 행렬
        for i in range(99):
            for j in range(1,100):
                if len(arr[cnt][i:i+j]) >= len(result) and arr[cnt][i:i+j] == arr[cnt][i+j-101:i-101:-1]:
                    result = arr[cnt][i:i+j]    #가장 긴 회문 문자열
        cnt += 1

    cnt = 0
    while cnt < 100:        #세로 행렬
        for i in range(99):
            for j in range(1,100):
                if len(arr2[cnt][i:i+j]) >= len(result) and arr2[cnt][i:i+j] == arr2[cnt][i+j-101:i-101:-1]:
                    result = arr2[cnt][i:i+j]      #가장 긴 회문 문자열
        cnt += 1

    print(f'#{tc} {len(result)}')