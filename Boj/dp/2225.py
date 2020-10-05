N, K = map(int, input().split())
dp = [[1 for _ in range(N+1)] for _ in range(K-1)]
dp = [[1]] + dp

for i in range(2, K):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[K-1]) % 1000000000)
