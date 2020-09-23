# sol 1.
N = int(input())
 for i in range(1, N + 1):
     print("*" * i + " " * (N - i) * 2 + "*" * i)
 for j in range(1, N):
     print("*" * (N - j) + " " * j * 2 + "*" * (N - j))



# sol. 2
N = int(input())
for i in range(-N + 1, N):
    print((" " * abs(2 * i)).center(2 * N, "*"))
