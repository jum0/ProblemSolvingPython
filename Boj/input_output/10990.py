N = int(input())
for i in range(N):
    print(" " * (N - i - 1) + (" " * (i * 2 - 1)).center(i * 2 + 1, "*"))

# 문자열에 음수 곱하면 문자열이 출력되지 않는다.
