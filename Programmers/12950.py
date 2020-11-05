# sol 1.
def solution(arr1, arr2):
    res = []
    
    for i in range(len(arr1)):
        res.append(list(map(sum, zip(arr1[i], arr2[i]))))
        
    return res
    
    
# sol 2.
def solution(arr1, arr2):
    res = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    
    return res
