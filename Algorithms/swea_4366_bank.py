T= int(input())
for tc in range(1, T+1):
    tw = input()
    thre = input()

    two_lst = []
    for m in range(len(tw)):
        two = list(tw)
        if two[m] == '0':
            two[m] = '1'
            two_lst.append(int(''.join(two), 2))
        else:
            two[m] = '0'
            two_lst.append(int(''.join(two), 2))

    three_lst = []
    for n in range(len(thre)):
        three = list(thre)
        if three[n] == '0':
            three[n] = '1'
            three_lst.append(int(''.join(three), 3))
            three[n] = '2'
            three_lst.append(int(''.join(three), 3))
        elif three[n] == '1':
            three[n] = '0'
            three_lst.append(int(''.join(three), 3))
            three[n] = '2'
            three_lst.append(int(''.join(three), 3))
        else:
            three[n] = '0'
            three_lst.append(int(''.join(three), 3))
            three[n] = '1'
            three_lst.append(int(''.join(three), 3))

    result = 0
    for k in two_lst:
        if k in three_lst:
            result = k
            break

    print(f'#{tc} {result}')

