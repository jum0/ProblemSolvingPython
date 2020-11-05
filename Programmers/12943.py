def solution(num):
    cnt = 0
    
    for _ in range(500):
        if num == 1:
            break
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        cnt += 1
    
    return -1 if num != 1 else cnt
