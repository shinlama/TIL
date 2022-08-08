T = 10

for TC in range(1, T+1):
    row = int(input())
    column = list(map(int, input().split()))
    result = 0
    for i in range(2, row -2):
        if (column[i] > column[i-2]) and (column[i] > column[i-1]) and (column[i] > column[i+1]) and (column[i] > column[i+2]):
            max_column = column[i-2]
            for j in range(-2, 3):
                if j == 0:
                    continue
                if column[i-j] > max_column:
                    max_column = column[i-j]
            result += column[i] - max_column
    print('#{0} {1}'.format (TC, result))
