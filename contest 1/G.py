n = int(input())
array = list(range(1, n + 1))

for i in range(2, n):
    (array[i], array[i // 2]) = (array[i // 2], array[i])

print(' '.join(map(str, array)))