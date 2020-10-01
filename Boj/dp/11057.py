N = int(input())
dp = [[1 for col in range(10)] for row in range(N+1)]

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:10])

print(sum(dp[N]) % 10007)
