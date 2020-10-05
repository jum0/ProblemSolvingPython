dp = [0, 1, 1, 1, 2] + [0] * 96
for _ in range(int(input())):
    N = int(input())
    for i in range(5, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])
