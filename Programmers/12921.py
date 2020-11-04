# sol 1.
def solution(n):
    chk_lst = [False, False] + [True for _ in range(n-1)]
    
    for i in range(2, n+1):
        if chk_lst[i]:
            for j in range(i+i, n+1, i):
                chk_lst[j] = False
    
    return sum(chk_lst)

# sol 2.
def solution(n):
    nums = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in nums:
            nums -= set(range(i+i, n+1, i))
    
    return len(nums)
