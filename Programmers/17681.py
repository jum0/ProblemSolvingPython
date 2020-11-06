# goal

# description
# 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ) 또는벽(#") 두 종류
# 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽
# 지도 1과 지도 2는 각각 정수 배열로 암호화
# 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열

# condition
# 1 ≦ n ≦ 16
# arr1, arr2는 길이 n인 정수 배열
# 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족

# sol 1.
def solution(n, arr1, arr2):
    res = []
    
    # zip으로 묶어서 두개 비트 연산한 리스트 만들기, 앞의 0b 처리
    arr_calculate_or = [bin(a | b)[2:] for a, b in zip(arr1, arr2)]
    #개수가 5개 안되는 애들은 앞에 다 0 넣기
    arr_add_zero = list(map(lambda x: (n-len(x))*'0'+x, arr_calculate_or))
    # 0은 공백으로 1은 #으로 변경
    res = [''.join(['#' if s == '1' else ' ' for s in i]) for i in arr_add_zero]
    
    return res


# sol 2.
def solution(n, arr1, arr2):
    res = []
    
    # zip으로 묶어서 두개 비트 연산한 리스트 만들기, 앞의 0b 처리
    arr_calculate_or = [bin(a | b)[2:] for a, b in zip(arr1, arr2)]
    #개수가 5개 안되는 애들은 앞에 다 0 넣기
    arr_add_zero = [s.rjust(n, '0') for s in arr_calculate_or]
    # 0은 공백으로 1은 #으로 변경
    res = [s.replace('0', ' ').replace('1', '#') for s in arr_add_zero]

    return res
