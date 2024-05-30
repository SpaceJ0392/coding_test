def max_profit(N, profits):
    # 초기화: 첫 날의 이익을 현재 최대 및 전역 최대값으로 설정
    current_max = global_max = profits[0]
    
    for i in range(1, N):
        # 현재까지의 최대 이익을 계산
        current_max = max(profits[i], current_max + profits[i])
        # 전역 최대 이익을 갱신
        global_max = max(global_max, current_max)
    
    return global_max

# 입력 받기
N = int(input())
profits = list(map(int, input().split()))

# 결과 출력
print(max_profit(N, profits))
