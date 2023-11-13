def get_arounds(target, a):
    target_idx = a.index(target)

    left_list = a[:target_idx]
    right_list = a[target_idx + 1 :]

    if len(left_list) != 0 and len(right_list) == 0:
        return min(left_list), max(a) + 1
    elif len(left_list) == 0 and len(right_list) != 0:
        return max(a) + 1, min(right_list)

    return min(left_list), min(right_list)


def solution(a):
    answer = 0

    for target in a:
        left, right = get_arounds(target, a)

        if target < left and target < right:
            continue

        answer += 1

    return answer


print(solution(	[-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))

# 알고리즘
# 기준 값을 기준으로 양쪽을 다른 리스트로 처리하여, 왼쪽, 오른쪽 리스트를 만든다.
# (왼쪽 리스트의 경우, reverse한다.)

# 각 리스트의 첫번째 값과 두번째 값을 비교하여, 큰쪽만 남기는 연산을 len(1)이 될 때 까지 반복한다.

# 연산이 완료된 두 리스트의 하나의 값에 대해 지정된 값보다 둘다 작으면 기준 값은 하나의 값이 될 수 없음...
