def solution(strings, n):
    return sorted(strings, key = lambda str: (str[n], str))
