def solution(d, budget):
    cnt = 0
    
    for i in sorted(d):
        if budget - i >= 0:
            budget -= i
            cnt += 1
            
    return cnt
