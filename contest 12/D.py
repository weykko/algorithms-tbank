n = int(input())
result, twos, fives = 1, 0, 0

for i in range(1, n + 1):
    while i % 2 == 0:
        twos += 1
        i //= 2
    while i % 5 == 0:
        fives += 1
        i //= 5
    result *= i
    result %= 10

for _ in range(twos - fives):
    result *= 2
    result %= 10

print(result)
