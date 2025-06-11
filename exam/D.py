def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for k in range(i * 2, n + 1, i):
                prime[k] = False

    return prime


MOD = 10 ** 9 + 9
n = int(input())
sieve_prime = sieve(999)
primes = set(e for e in range(100, 1000) if sieve_prime[e])

dp = [0] * 1000
for prime in primes:
    dp[prime] = 1

for _ in range(n - 3):
    new_dp = [0] * 1000
    for num in range(100, 1000):
        if dp[num] == 0: continue
        for digit in range(10):
            new_num = (num % 100) * 10 + digit
            if new_num in primes:
                new_dp[new_num] = (new_dp[new_num] + dp[num]) % MOD

    dp = new_dp

result = sum(dp) % MOD
print(result)