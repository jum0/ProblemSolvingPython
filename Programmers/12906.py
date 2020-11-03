# sol 1.
def solution(arr):
    answer = []
    for idx, a in enumerate(arr):
        if idx == 0:
            answer.append(a)
        if a != answer[-1]:
            answer.append(a)
        
    return answer

# sol 2.
def solution(arr):
     answer = []
     for i in arr:
         if answer[-1:] == [i]: continue
         answer.append(i)
    
     return answer
