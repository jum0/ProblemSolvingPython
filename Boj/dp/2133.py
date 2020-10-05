N = int(input())
dp = [1] + [0] * 30
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 + sum(dp[:i-3]) * 2

print(dp[N])
