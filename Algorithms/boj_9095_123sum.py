T = int(input())
def A(n):
    if n ==1:
        return 1
    elif n ==2:
        return 2
    elif n ==3:
        return 4
    elif n>=4:
        return A(n-1) + A(n-2) + A(n-3)

for tc in range(1, T+1):
    N = int(input())
    print(A(N))