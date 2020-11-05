# sol 1.
def solution(n, m):
    a, b = min(n, m), max(n, m)
    res = [i for i in range(1, a + 1) if a % i == 0]
    g = max([r for r in res if b % r == 0])
    
    return [g, a * b / g]

# sol 2.
def solution(n, m):
    high, low = max(n, m), min(n, m)
    reminder = 1
    
    while reminder:
        reminder = high % low
        high = low
        low = reminder
    
    return [high, n * m / high]
        
