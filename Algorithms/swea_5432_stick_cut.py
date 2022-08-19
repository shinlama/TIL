T = int(input())
for tc in range(1, T+1):
    stick = input()
    pipe = 0
    result = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            pipe += 1
        else:
            pipe -= 1
            if stick[i-1]=='(':
                result += pipe
            else:
                result += 1
    print(f'#{tc} {result}')