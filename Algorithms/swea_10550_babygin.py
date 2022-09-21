T = int(input())
for tc in range(1, T+1):
    num = int(input())
    lst = [0] * 12

    for i in range(6):
        lst[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0
    while i < 10:
        if lst[i] >= 3:
            lst[i] -= 3
            tri += 1
            continue
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:
            lst[i+1] -= 1
            lst[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2 :
        print(f"#{tc} Baby Gin")
    else:
        print(f"#{tc} Lose")