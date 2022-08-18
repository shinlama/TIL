T = int(input())

for tc in range(1, T+1):
    s = input()
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack += s[i]
        elif s[i] != stack[-1]:
            stack += s[i]
        else:
            stack.pop()

    print(f'#{tc} {len(stack)}')