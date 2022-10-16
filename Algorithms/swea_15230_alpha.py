T = int(input())

alpha = list('abcdefghijklmnopqrstuvwxyz')
for tc in range(1, T+1):
    str = input()
    cnt = 0
    for i in range(len(str)-1):
        if str[i] == alpha[i] and str[i+1] == alpha[i+1]:
            cnt += 1

    cnt += 1
    if cnt == 1:
        cnt = 0

    print(f'#{tc} {cnt}')