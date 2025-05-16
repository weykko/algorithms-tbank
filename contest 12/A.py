def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


n, k = map(int, input().split())
print(lcm(n, k))
