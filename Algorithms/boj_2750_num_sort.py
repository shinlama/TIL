T = int(input())

arr= []
for tc in range(1, T+1):
    arr.append(int(input()))

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

for x in arr:
    print(x)