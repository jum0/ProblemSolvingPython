# sol 1.
def solution(n):
    return "수박" * (n//2) + "수" * (n%2)

# sol 2.
def solution(n):
    return ("수박" * n)[:n]
