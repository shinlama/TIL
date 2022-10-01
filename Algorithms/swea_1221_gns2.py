import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())
dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5,
       "SIX":6, "SVN":7, "EGT":8, "NIN":9}
dic2 = dict(map(reversed, dic.items()))

for tc in range(1, T+1):
    tc, n = input().split()
    n = int(n)

    lst = list(input().split())
    num = []
    for str in lst:
        num.append(dic[str])
        num.sort()

    str = []
    for i in num:
        str.append(dic2[i])

    print(tc)
    print(*str)