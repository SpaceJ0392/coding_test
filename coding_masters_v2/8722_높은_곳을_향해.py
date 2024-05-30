
def max_jumps(N, heights):
    # DP 배열 초기화
    dp = [1] * N
    
    # LIS 알고리즘 적용
    for i in range(1, N):
        for j in range(i):
            if heights[i] > heights[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 최대 점프 횟수는 dp 배열의 최댓값 - 1
    return max(dp) - 1

# 입력 받기
N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(max_jumps(N, heights))
