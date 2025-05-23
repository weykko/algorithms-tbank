def find_factorials(n, p):
    factorials = [1]

    for i in range(1, n + 1):
        factorials.append((factorials[-1] * i) % p)

    return factorials


def fast_power_mod(a, b, p):
    res = 1
    while b != 0:
        if b & 1:
            res = (res * a) % p
        a = (a * a) % p
        b //= 2

    return res


def get_inv_factorial(factorials, n, p):
    return fast_power_mod(factorials[n], p - 2, p)


def cnk(factorials, n, k, p):
    return (factorials[n] * get_inv_factorial(factorials, n - k, p)) % p * get_inv_factorial(factorials, k, p) % p


p = 10 ** 9 + 7
n, k = map(int, input().split())
print(cnk(find_factorials(n, p), n, k, p))
