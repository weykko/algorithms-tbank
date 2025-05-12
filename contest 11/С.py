s = input()
n = len(s)
dp = [[''] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = s[i]

res = 0
palindrome = ''
for ln in range(2, n + 1):
    for l in range(0, n - ln + 1):
        r = l + ln - 1
        if s[l] == s[r]:
            dp[l][r] = f'{s[l]}{dp[l + 1][r - 1]}{s[r]}'
        else:
            if len(dp[l + 1][r]) > len(dp[l][r - 1]):
                dp[l][r] = dp[l + 1][r]
            else:
                dp[l][r] = dp[l][r - 1]
        if len(dp[l][r]) > res:
            res = len(dp[l][r])
            palindrome = dp[l][r]

if n == 1:
    print(1)
    print(s)
else:
    print(res)
    print(palindrome)
