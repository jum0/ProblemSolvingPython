# sol 1.
def solution(n):
    return [int(i) for i in str(n)[::-1]]

# sol 2.
def solution(n):
    return list(map(int, reversed(str(n))))
