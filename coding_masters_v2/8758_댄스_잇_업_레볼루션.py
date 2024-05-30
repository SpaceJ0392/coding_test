def can_alternate_steps(pattern):
    """
    주어진 패턴을 번갈아 밟을 수 있는지 판별하는 함수

    Args:
        pattern: 발판 패턴 리스트

    Returns:
        번갈아 밟을 수 있으면 "OK", 아니면 "NG"
    """
    N = len(pattern)
    current_angle = 0  # 현재 시선 각도
    left_foot = True  # 왼발로 시작하는지 여부

    for i in range(N):
        next_step = pattern[i]
        target_angle = (next_step - 1) * 90  # 다음 발판의 각도

        # 현재 발과 다음 발판의 각도 차이 계산
        diff_angle = (target_angle - current_angle) % 360
        if diff_angle > 180:
            diff_angle = 360 - diff_angle

        # 180도를 초과하는 회전이 필요한 경우
        if diff_angle > 180:
            return "NG"

        # 다음 발판으로 이동 후 현재 발과 각도 업데이트
        current_angle = target_angle
        left_foot = not left_foot

    return "OK"

# 입력 받기
N = int(input())
pattern = list(map(int, input().split()))

# 패턴 판별 및 출력
result = can_alternate_steps(pattern)
print(result)
