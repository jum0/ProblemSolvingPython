def solution(s, n):
    res =""
    
    for i in s:
        tmp = " "
        if i.isupper():
            tmp = chr((ord(i) + n - 65) % 26 + 65)
        elif i.islower():
            tmp = chr((ord(i) + n - 97) % 26 + 97)
        res += tmp
    
    return res
