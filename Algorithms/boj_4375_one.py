while True:
    try:
        n = int(input())
    except:
        break

    num = 0
    cnt = 1
    while True:
        num = num * 10 + 1
        num = num % n
        if num == 0:
            print(cnt)
            break
        cnt += 1

# #숏코딩
# import sys
# def f(n,i=1):
#   while i % int(n) != 0:
#     i = i * 10 + 1
#   print(len(str(i)))

# *map(f,sys.stdin),