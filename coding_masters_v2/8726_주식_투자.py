def count_ways(N, K):
    # 수익은 -100*N에서 100*N까지 가능하므로 이를 인덱스로 사용하기 위해 오프셋을 사용
    OFFSET = 100 * N
    
    # 동적 계획법 테이블 초기화
    dp = [[0] * (2 * OFFSET + 1) for _ in range(N + 1)]
    dp[0][OFFSET] = 1  # 시작점: 수익 0을 OFFSET 위치에 저장
    
    for i in range(1, N + 1):
        for j in range(-100 * N, 100 * N + 1):
            if j + OFFSET - 100 >= 0:
                dp[i][j + OFFSET] += dp[i - 1][j + OFFSET - 100]
            if j + OFFSET + 100 <= 2 * OFFSET:
                dp[i][j + OFFSET] += dp[i - 1][j + OFFSET + 100]
    
    return dp[N][K + OFFSET] if -100 * N <= K <= 100 * N else 0

# 입력 받기
N, K = map(int, input().strip().split())

# 결과 출력
print(count_ways(N, K))
