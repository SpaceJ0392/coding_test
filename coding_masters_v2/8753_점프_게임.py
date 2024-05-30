def count_jump_cases(N, jumps):
    """
    점프 게임 종료 경우의 수를 계산하는 함수

    Args:
        N: 칸의 개수
        jumps: 각 칸의 점프 제한 리스트

    Returns:
        점프 게임 종료 경우의 수를 1,000,000,007로 나눈 나머지
    """
    MOD = 1000000007
    dp = [0] * (N + 1)  # dp[i]: i번 칸까지 도달하는 경우의 수
    dp[1] = 1  # 1번 칸에는 무조건 도달

    for i in range(1, N):
        for j in range(i + 1, min(i + jumps[i] + 1, N + 1)):
            dp[j] = (dp[j] + dp[i]) % MOD  # i번 칸에서 j번 칸으로 점프하는 경우 추가

    return dp[N]

# 입력 받기
N = int(input())
jumps = [0] + list(map(int, input().split()))  # 0번 인덱스는 사용하지 않음

# 점프 게임 종료 경우의 수 계산 및 출력
result = count_jump_cases(N, jumps)
print(result)
