def solution(n, lost, reserve):
    clothes = [0] + [1 for i in range(n)]
    
    for i in lost:
        clothes[i] -= 1
    for i in reserve:
        clothes[i] += 1
    for i in range(1, n+1):
        # 상태확인
        if clothes[i] == 0:
            #앞에서 확인
            if clothes[i-1] > 1:
                clothes[i-1] -=1
                clothes[i] += 1
        #상태 확인
        if clothes[i] == 0:
            #맨 뒤면 뒤가 없으니깐 제외
            if i != n and clothes[i+1] > 1:
                clothes[i+1] -= 1
                clothes[i] += 1
        
    return len([c for c in clothes if c > 0])
