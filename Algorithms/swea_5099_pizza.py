T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    j = list(map(int,input().split()))
    lst = []
    for i in range(M):
        lst.append([i+1,j[i]])          #인덱스와 치즈값으로 이차원 배열 만들기

    pizza = []
    for k in range(N):                  #N개 크기의 화덕 리스트
        pizza.append(lst.pop(0))

    while len(pizza) >= 2:
        a, b = pizza.pop(0)
        if b // 2 > 0:                  #0 될때까지 2로 나눠줌
            pizza.append((a, b//2))
        if lst and len(pizza)!= N:      #개수 맞춰서 넣어줌
            pizza.insert(0, lst.pop(0))

    print(f'#{tc} {pizza[0][0]}')        #마지막 남아있는 치즈의 인덱스
