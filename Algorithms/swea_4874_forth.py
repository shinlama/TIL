T = int(input())

for tc in range(1, T+1):
    s = input().split()[:-1]
    st = []

    for str in s:
        if str.isdigit():
            st.append(int(str))
        elif str in ['+', '-', '/', '*']:
            try:
                b = st.pop()
                a = st.pop()
                if str == '+':
                    st.append(a+b)
                elif str == '*':
                    st.append(a*b)
                elif str == '-':
                    st.append(a-b)
                elif str == '/':
                    st.append(a//b)

            except:
                result = 'error'
                break
        result = st[0]
    if len(st)>=2:
        result = 'error'
    print(f'#{tc} {result}')