def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리
    bridge = [0 for _ in range(bridge_length)]
    while bridge:
        answer += 1
        bridge.pop()
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.insert(0, truck_weights.pop(0))
            else:
                bridge.insert(0, 0)
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
