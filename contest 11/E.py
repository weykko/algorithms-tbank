s = input().strip()
n = len(s)
dp = [[''] * n for _ in range(n)]

for length in range(1, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        min_str = s[l:r + 1]
        if length > 4:
            for k in range(l, r):
                str = dp[l][k] + dp[k + 1][r]
                if len(str) < len(min_str): min_str = str
            for p in range(1, length):
                if length % p == 0 and all(s[i] == s[i - p] for i in range(l + p, r + 1)):
                    str = f'{length // p}({dp[l][l + p - 1]})'
                    if len(str) < len(min_str): min_str = str
        dp[l][r] = min_str

print(dp[0][n - 1])
