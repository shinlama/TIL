import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr[::-1]))

    word_lst = []
    word_lst2 = []
    for l in range(100, 0, -1):
        for i in range(100):
            for j in range(100):

                if j + l < 100:
                    word = arr[i][j:j+l]
                    word2 = arr2[i][j:j+l]
                    if word == word[::-1]:
                        word_lst.append(word)
                        break
                    if word2 == word2[::-1]:
                        word_lst2.append(word2)
                else:
                    continue

    print(f'#{tc} {max(len(word_lst[0]), len(word_lst2[0]))}')