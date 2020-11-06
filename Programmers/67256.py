def solution(numbers, hand):
    res = ''
    l = 10
    r = 12
    
    for n in numbers:
        # 정해져 있는 경우 [1, 4, 7] / [3, 6, 9]
        if n in [1, 4, 7]:
            l = n
            res += 'L'
        elif n in [3, 6, 9]:
            r = n
            res += 'R'
        
        # 거리를 판단해야 하는 경우 [2, 5, 8, 0]
        else:
            # 거리 계산
            l_d = 0
            r_d = 0
            
            # n이 0인 경우도 고려
            if n == 0:
                n = 11
            
            # 왼손 거리
            tmp_l = l
            while tmp_l not in [n-1, n, n+1]:
                # n(다음 숫자)이 더 위쪽에 있는 경우
                # n(다음 숫자)이 더 아래쪽에 있는 경우
                tmp_l = tmp_l - 3 if n < l else tmp_l + 3
                l_d += 1
            l_d = l_d + abs(n - tmp_l)
            
            # 오른손 거리
            tmp_r = r
            while tmp_r not in [n-1, n, n+1]:
                # n(다음 숫자)이 더 위쪽에 있는 경우
                # n(다음 숫자)이 더 아래쪽에 있는 경우
                tmp_r = tmp_r - 3 if n < r else tmp_r + 3
                r_d += 1
            r_d = r_d + abs(n - tmp_r)
            
            # 거리가 같은 경우
            if l_d == r_d:
                if hand == 'right':
                    r = n
                    res += 'R'
                else:
                    l = n
                    res += 'L'
            # 거리가 다른 경우
            else:
                # 왼손이 더 가까운 경우
                if l_d < r_d:
                    l = n
                    res += 'L'
                else:
                    r = n
                    res += 'R'
    
    return res
    
