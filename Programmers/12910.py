def solution(arr, divisor):
    answer = sorted(i for i in arr if i % divisor == 0)
    return [-1] if not answer else answer
