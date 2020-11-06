# goal
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수

# description
# 실패율 - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수

# condition
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

import collections

def solution(N, stages):
    total = len(stages)
    dic = {}
    # counter 함수 통해서 각 숫자별 개수 구하기
    stages_counter = collections.Counter(stages)
    
    # 1부터 N+1까지 돌려서 dic에 key(숫자) value(실패율)로 넣기 total에서 이전 숫자만큼 분모 빼면서 넣기
    # 끝까지 통과한 애들은 필요 없어서 N+1.
    for i in range(1, N+1):
        dic[i] = 0 if stages_counter[i] == 0 else stages_counter[i]/total
        total -= stages_counter[i]
    
    return [k for k, v in sorted(dic.items(), reverse=True, key=lambda x: x[1])]
