from collections import deque


# idea : '다리'의 무게와 '다리'에 대한 리스트를 동시에 갱신시키며 값을 구한다.
# 트럭이 '다리'에서 빠져나가는 부분(앞)과 트럭에서 빼내어 다리에 붙여주는 부분(뒤)가 구현되어야 함. -> deque 특성


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)  # 다리 크기만큼의 deque    [0,0]
    truck_weights = deque(truck_weights)  # 트럭 deque     [7,4,5,6]
    bridge_weight = sum(bridge)  # bridge deque 에 들어있는 총합     현재: 0

    while bridge:
        bridge_weight -= bridge[0]  # 가장 앞 쪽에 있는 트럭을 지워주기 위함
        bridge.popleft()  # 위와 동일
        answer += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:  # 트럭이 다리에 올라올 수 있음.
                bridge_weight += truck_weights[0]  # 앞에 있는 트럭을 브릿지 무게에 더해줌(올라오니까))
                bridge.append(truck_weights.popleft())  # 위와 동일
            else:
                bridge.append(0)  # 무게 크면 그대로 대기

    return answer