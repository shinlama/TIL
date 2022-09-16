# def divisor_sum(N):
#     summ = 0
#     num = 1
#     while num <= N:
#         if N % num == 0:
#             summ += num
#         num += 1
#     return summ

# def G(n):
#     if n <= 1:
#         return 1
#     else:
#         return G(n-1) + divisor_sum(n)

# T = int(input())
# print(G(T))


#숏코드
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += (n//i)*i
print(sum)