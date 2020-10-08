s = input()
dp = [0] * len(s)

if int(s[0]) > 0:
    dp[0] = 1

    for i in range(1, len(s)):
        if int(s[i]) > 0:
            dp[i] = dp[i-1]
        if 9 < int(s[i-1] + s[i]) <  27:
            if i == 1:
                dp[i] += 1
                continue
            dp[i] += dp[i-2]

print(dp[len(s) - 1] % 1000000)
