A = int(input())
x = list(input())[::-1]
sum = 0
for i in range(3):
    n = A * int(x[i])
    print(n)
    sum += n * 10**i
print(sum)