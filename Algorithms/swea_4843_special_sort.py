T = int(input())

def special_sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(0,i):
            if num[j]>num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split())) #input
    arr = special_sort(arr)

    result = []
    for i in range(5):
        # 가장 큰값 먼저 추출
        result.append(arr[len(arr) - 1 - i])
        # 가장 작은값 추출
        result.append(arr[i])

    # 공백으로 숫자 구분
    result = ' '.join(map(str, result))
    print(f"#{tc} {result}")