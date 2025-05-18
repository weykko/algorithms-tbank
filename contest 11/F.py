def get_coins(a, sum):
    n = len(a)
    coins = []

    for comb in range(3 ** n):
        cur_sum = 0
        cur_coins = []

        for i in range(n):
            d = comb % 3
            cur_sum += a[i] * d
            cur_coins.extend([a[i]] * d)
            comb //= 3

        if cur_sum == sum and (len(cur_coins) < len(coins) or not coins):
            coins = cur_coins

    return coins


n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) * 2 < n:
    print(-1)
else:
    coins = get_coins(a, n)
    if coins:
        print(len(coins))
        print(' '.join(map(str, coins)))
    else:
        print(0)
