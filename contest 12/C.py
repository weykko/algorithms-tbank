def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for k in range(i * 2, n + 1, i):
                prime[k] = False

    return prime


n = int(input())
prime = sieve(n)

for p in range(2, n // 2 + 1):
    if prime[p] and prime[n - p]:
        print(p, n - p)
        break
