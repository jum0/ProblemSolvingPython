# sol 1.
def solution(s):
    idx = 0
    res = ''
    
    for i in range(len(s)):
        tmp = s[i]
        if s[i].isalpha():
            if i == 0 or s[i-1] == ' ':
                idx = 0
                if s[i].isalpha():
                    tmp = s[i].upper()
            else:
                if idx % 2 == 0:
                    tmp = s[i].upper()
                else:
                    tmp = s[i].lower()
        res += tmp
        idx += 1
                
    return res

# sol 2.
def solution(s):
    return " ".join(map(lambda x: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(x)]), s.split(" ")))
