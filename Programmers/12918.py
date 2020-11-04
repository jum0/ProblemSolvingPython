# sol 1.
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

# sol 2.
def solution(s):
    return len(s) in [4, 6] and s.isdigit()

# sol 3.
def solution(s):
    return len(s) in (4, 6) and s.isdigit()
