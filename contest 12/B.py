import math

n = int(input())
primes = {}

for d in range(2, int(math.sqrt(n)) + 1):
    while n % d == 0:
        primes[d] = primes.get(d, 0) + 1
        n //= d

if n > 1: primes[n] = 1

result = '*'.join(f"{p}^{c}" if c > 1 else f"{p}" for p, c in primes.items())
print(result)