lst = [int(input()) for _ in range(10)]

result = []
for i in lst:
    result.append(i%42)

result = set(result)
print(len(result))