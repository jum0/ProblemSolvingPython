N = int(input())
for i in range(N):
	print(" " * (N - i - 1) + "*" * (i * 2 + 1))
for j in range(N - 1):
	print(" " * (j + 1) + "*" * ((N - j) * 2 - 3))
