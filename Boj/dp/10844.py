# sol 1.
N = int(input())
dp = [[0] + [1 for col in range(9)] for row in range(N+1)]

for i in range(2, N+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)



# sol 2.
N = int(input())
dp = [0] + [1 for _ in range(9)]

for _ in range(2, N+1):
    pre = dp.copy()
    dp[0] = pre[1]
    dp[9] = pre[8]
    for i in range(1, 8+1):
        dp[i] = pre[i-1] + pre[i+1]
    pre = dp.copy()

print(sum(dp) % 1000000000)
