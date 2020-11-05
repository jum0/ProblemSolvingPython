# goal
# 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴

# condition
# x는 -10000000 이상, 10000000 이하인 정수
# n은 1000 이하인 자연수

# sol 1.
def solution(x, n):
    if x == 0:
        return [0 for _ in range(n)]
    return [i for i in range(x, x*n+1, x)] if x > 0 else [i for i in range(x, x*n-1, x)]
    
# sol 2.
def solution(x, n):
    return [i * x + x for i in range(n)]
