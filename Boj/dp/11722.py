N = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(0, i):
        if arr[i] < arr[j] and dp[i] == dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))
