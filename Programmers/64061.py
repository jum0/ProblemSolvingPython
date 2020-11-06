# goal
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성

# condition
# 인형이 없는 칸은 빈칸
# 인형은 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다
# 집어 올린 인형은 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다.
# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다.
# 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
# board 배열은 2차원 배열로 크기는 5 x 5 이상 30 x 30 이하
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
#       0은 빈 칸을 나타냅니다.
#       1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
    

def solution(board, moves):
    basket = []
    moves = list(map(lambda x: x-1, moves))
    cnt = 0
    
    # floor 0이 제일 높아
    for m in moves:
        for floor in board:
            if floor[m] != 0:
                basket.append(floor[m])
                # check basket
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    cnt += 2
                floor[m] = 0
                break
                
    return cnt
