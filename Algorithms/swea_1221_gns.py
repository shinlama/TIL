T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    arr = list(input().split())
    num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, "FOR":4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    num2 = {v: k for k, v in num.items()}

    string = []
    for i in arr:
        string.append(num[i])
        string.sort()

    string2 = []
    for j in string:
        string2.append(num2[j])

    print(N)
    print(*string2)