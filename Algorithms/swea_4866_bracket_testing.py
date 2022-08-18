T = int(input())

for tc in range(1,T+1):
    my_str = input()
    stack = []
    result = 1
    for i in my_str:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if len(stack) == 0: 		# ( 나 { 없으면
                result = 0
                break
            else:
                j = stack.pop()    #없애기
                if i == ')' and j == '{':
                    result = 0
                elif i == '}' and j == '(':
                    result = 0

    if len(stack) != 0:
        result = 0
    print(f'#{tc} {result}')