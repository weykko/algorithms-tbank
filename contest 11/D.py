l, n = map(int, input().split())
cuts = [0] + list(map(int, input().split())) + [l]
n += 2
dp = [[0] * n for _ in range(n)]

for j in range(2, n):
    for i in range(j - 2, -1, -1):
        dp[i][j] = float('inf')

        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        dp[i][j] += cuts[j] - cuts[i]

print(dp[0][n - 1])
