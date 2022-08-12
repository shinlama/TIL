def isPrime(n):
    if memo[n] != -1:
        return memo[n]
    else:
        if n == 2 :
            memo[n] = 1
        elif n %2 == 0:
            memo[n] = 0
        else:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    memo[n] = 0
                    break
                i += 1
            else:
                memo[n] = 1
        return memo[n]


def isPrime(n):
    if n ==2 :
        return 1
    elif n%2 == 0:
        return 0
    else:
        i = 2
        while i*i <= n:
            if n % i == 0 :
                return 0
            i += 1
        else:
            return 1

memo = [-1] * 1000000
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    s = 0
    for n in range(a+1, b):
        s += n * primenumber(n)
    print(f'#{tc} {s}')