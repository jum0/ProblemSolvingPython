def solution(arr):
    m = sorted(arr)[0]
    return [-1] if len(arr) == 1 else [i for i in arr if i > m]
