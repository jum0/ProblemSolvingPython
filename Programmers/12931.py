# sol 1.
def solution(n):
    res = 0
    while(n):
        res += n % 10
        n = n // 10
    
    return res

# sol 2.
def solution(n):
    return sum([int(i) for i in str(n)])
