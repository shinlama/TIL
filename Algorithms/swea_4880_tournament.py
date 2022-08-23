def f(i, j):            #이기는 인덱스
    if i == j:
        return i
    else:
        left = f(i, (i+j)//2)
        right = f((i+j)//2+1, j)
        return win(left, right)

def win(l, r):          #이기는 숫자의 인덱스 반환
    if (lst[l] - lst[r]) in [-2,1] or (lst[l]==lst[r]):			#1,3일 때 1이 승, 2,1일 때 1이 승, 같을 때는 앞의 인덱스 반환
        return l
    else:
        return r

T = int(input())
for tc in range(1, T+1):
    N = int(input())        #인덱스 하나 앞에 추가해주기
    lst = [0] + list(map(int,input().split()))

    print(f'#{tc} {f(1,N)}')