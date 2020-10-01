n = int(input())
arr = [0 for _ in range(n+3)]
dp = arr.copy()

for i in range(3, n+3):
    arr[i] = int(input())
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

print(max(dp))
