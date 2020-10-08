N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * len(P)

for i in range(1, N+1):
    dp[i] = P[i]
    for j in range(1, i):
        if dp[j] + P[i-j] > dp[i]:
            dp[i] = dp[j] + P[i-j]

print(dp[N])
