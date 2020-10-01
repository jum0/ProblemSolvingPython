for _ in range(int(input())):
    n = int(input())
    upper = [0, 0] + list(map(int, input().split()))
    lower = [0, 0] + list(map(int, input().split()))
    dp = [upper, lower]

    for i in range(2, n+2):
        dp[0][i] = max(dp[1][i-2] + dp[0][i], dp[1][i-1] + dp[0][i])
        dp[1][i] = max(dp[0][i-2] + dp[1][i], dp[0][i-1] + dp[1][i])

    print(max(dp[0][n+1],dp[1][n+1]))
