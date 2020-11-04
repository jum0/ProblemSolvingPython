# sol 1.
def solution(s):
    p_count = 0
    y_count = 0
    
    for i in s.lower():
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1

    return True if p_count == y_count else False

# sol 2.
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
