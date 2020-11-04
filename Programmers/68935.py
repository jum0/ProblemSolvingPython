def solution(n):
    res = 0
    n_3 = ""
    
    while(n):
        n_3 = str(n%3) + n_3
        n = n // 3
    for idx, n in enumerate(n_3):
        res += 3 ** idx * int(n)
    
    return res
