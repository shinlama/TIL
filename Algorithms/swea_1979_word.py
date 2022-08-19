T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr[::-1]))  # 가로 세로 바꾼 이차원 행렬 만들기

    result = 0
    for i in range(len(arr)):  # 빈 문자열에 넣기
        st = ''
        for j in range(len(arr[i])):
            st += str(arr[i][j])
        for k in st.split('0'):  # 0 기준으로 자른 리스트 생성
            if k == '1' * K:
                result += 1
    result2 = 0
    for i in range(len(arr2)):  # arr2도 똑같이
        st2 = ''
        for j in range(len(arr2[i])):
            st2 += str(arr2[i][j])
        for k in st2.split('0'):
            if k == '1' * K:
                result2 += 1

    print(f'#{tc} {result + result2}')