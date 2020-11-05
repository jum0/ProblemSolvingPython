# sol 1.
def solution(phone_number):
    res = ''
    for idx, n in enumerate(phone_number):
        res += '*' if len(phone_number) - 4 > idx else n
    
    return res
    
# sol 2.
def solution(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]
