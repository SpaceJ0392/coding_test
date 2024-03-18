def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve_list = [0] * ((len(reserve) + len(lost)) + 1)

    for num in reserve:
        reserve_list[num] = num

    for target in lost:
        l_idx, r_idx = target - 1, target + 1

        # 경계 설정
        if l_idx < 0 and r_idx <= len(reserve_list):
            if reserve_list[r_idx] != 0:
                answer += 1
                reserve_list[r_idx] = 0
            continue

        if r_idx > len(reserve_list) and l_idx >= 0:
            if reserve_list[l_idx] != 0:
                answer += 1
                reserve_list[l_idx] = 0
            continue

        if reserve_list[l_idx] != 0:
            answer += 1
            reserve_list[l_idx] = 0
            continue

        if reserve_list[r_idx] != 0:
            answer += 1
            reserve_list[r_idx] = 0
            continue

    return answer


print(solution(5, [2, 4], [3]))
