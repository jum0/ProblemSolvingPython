def solution(x):
    sum_x = sum([int(i) for i in str(x)])
    
    return True if x % sum_x == 0 else False # sol 1.
    return x % sum_x == 0                    # sol 2.
