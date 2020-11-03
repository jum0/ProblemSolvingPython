# sol 1.
def solution(array, commands):
    result = []
    
    for c in commands:
        new_array = array[c[0]-1:c[1]]
        new_array.sort()
        result.append(new_array[c[2]-1])
        
    return result

# sol 2.
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
