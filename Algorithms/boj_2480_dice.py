dice = sorted(list(map(int, input().split())))
set_dice = set(dice)


if len(set_dice) == 1:
    ans = 10000 + dice[0] * 1000
elif len(set_dice) == 3:
    ans = max(dice) * 100
else:
    for i in range(2):
        if dice[i] == dice[i+1]:
            j = dice[i]
            ans = 1000 + j* 100


print(ans)