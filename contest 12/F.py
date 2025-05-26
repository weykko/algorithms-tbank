def fast_power_mod(a, b, p):
    res = 1
    while b != 0:
        if b & 1:
            res = (res * a) % p
        a = (a * a) % p
        b //= 2

    return res


n, m, k, MOD = map(int, input().split())
result = fast_power_mod(m, n, MOD) * fast_power_mod(k, MOD - 2, MOD) % MOD
print(result)
