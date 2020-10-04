lst = [0, 0, 0]
for _ in range(int(input())):
    lst.append(int(input()))
dp = [0 for _ in range(len(lst))]

for i in range(3, len(dp)):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

print(dp[-1])
