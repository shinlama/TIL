T = 10

for tc in range(1, T+1):
    N = int(input()) # 입력된 덤프 횟수
    box_list = list(map(int,input().split()))

    # 각 높이마다 몇 개가 있는지 카운팅 
    cnt = [0] * 101
    for i in box_list:
        cnt[i] += 1

    min = 101
    max = 0
    for box in box_list:
        if box < min :
            min = box
        if box > max :
            max = box

    # 각 높이마다 갯수가 달라짐
    n = 0
    while n < N :
        cnt[max] -= 1
        cnt[max-1] += 1
        cnt[min] -= 1
        cnt[min+1] += 1

        while cnt[max] == 0:
            max -= 1
        while cnt[min] == 0:
            min += 1

        n += 1

    print(f'#{tc} {max-min}')
