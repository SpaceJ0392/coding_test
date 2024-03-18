def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    now_bridge = 0

    while len(truck_weights) != 0:
        if len(bridge) == bridge_length:
            now_bridge -= bridge[0]
            bridge = bridge[1:]

        bridge.append(truck_weights[0])
        now_bridge += truck_weights[0]

        if now_bridge > weight:
            bridge.pop()
            bridge.append(0)
            now_bridge -= truck_weights[0]
        else:
            truck_weights = truck_weights[1:]

        answer += 1

    return answer + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
