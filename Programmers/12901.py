def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    return day_of_week[(sum(month[:a-1]) + b) % 7]
