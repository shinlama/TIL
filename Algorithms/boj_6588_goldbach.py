while True:
    flag = True
    n = int(input())
    if n == 0:
        break

    lst = []
    for i in range(3, n//2 +1):
        lst.append([i, n-i])

    lst2 = []
    for j in range(len(lst)):
        for k in range(2, int(lst[j][0] ** 0.5) +1):
            if lst[j][0] % k == 0:
                break
        for p in range(2, int(lst[j][1] ** 0.5) +1):
            if lst[j][1] % p == 0:
                break

        else:
            lst2.append(lst[j])

    a = lst2[0][0]
    b = lst2[0][1]
    print(f'{n} = {a} + {b}')
    flag = False

    if flag:
        print("Goldbach's conjecture is wrong.")