T = 2
for tc in range(1, T+1):
    n = int(input())
    s = input()

    #후위 표기식 만들기
    result = ''
    st = []
    for str in s:
        if str.isdigit():
            result += str
        else:
            if str == '(':
                st.append(str)
            elif str == '*':
                while st and st[-1] != '*':
                    result += st.pop()
                st.append(str)
            elif str == '+':
                while st and st[-1] != '(':
                    result += st.pop()
                st.append(str)
            elif str == ')':
                while st and st[-1] != '(':
                    result += st.pop()
                st.pop()
    while st:
        result += st.pop()

    #후위 표기식 계산
    #숫자면 result 문자열에, 연산자면 2개 pop 해서 연산하기
    st2 = []
    for x in result:
        if x.isdigit():
            st2.append(int(x))
        else:
            a = st2.pop()
            b = st2.pop()
            if x == '+':
                st2.append(a+b)
            if x == '*':
                st2.append(a*b)

    print(f'#{tc} {st2[0]}')