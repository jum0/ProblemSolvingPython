# goal
# a와 b의 내적을 return 하도록 solution 함수

# condition
# a, b의 길이는 1 이상 1,000 이하입니다.
# a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

def solution(a, b):
    return sum([a * b for a, b in zip(a, b)])
