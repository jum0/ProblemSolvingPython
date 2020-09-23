N = int(input())
for i in range(N - 1):
    print(" " * (N - i - 1) + (" " * (i * 2 - 1)).center(i * 2 + 1, "*"))
print("*" * (2 * N - 1))
