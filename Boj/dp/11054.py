# sol 1.
import copy

N = int(input())
arr_inc = list(map(int, input().split()))
arr_dec = copy.deepcopy(arr_inc)
arr_dec.reverse()

dp_inc = [1 for _ in range(N)]
dp_dec = copy.deepcopy(dp_inc)
dp_fin = []

for i in range(N):
    for j in range(0, i):
        if arr_inc[i] > arr_inc[j] and dp_inc[i] == dp_inc[j]:
            dp_inc[i] = dp_inc[j] + 1
        if arr_dec[i] > arr_dec[j] and dp_dec[i] == dp_dec[j]:
            dp_dec[i] = dp_dec[j] + 1

dp_dec.reverse()
for i in range(N):
    dp_fin.append(dp_inc[i] + dp_dec[i] - 1)

print(max(dp_fin))



# sol 2.
def sol(N, arr):
    dp = [1 for _ in range(N)]

    for i in range(N):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] == dp[j]:
                dp[i] = dp[j] + 1
    return dp

N = int(input())
arr_inc = list(map(int, input().split()))
arr_dec = arr_inc[::-1]

dp_inc = sol(N, arr_inc)
dp_dec = sol(N, arr_dec)[::-1]

print(max(map(sum, zip(dp_inc, dp_dec))) - 1)
