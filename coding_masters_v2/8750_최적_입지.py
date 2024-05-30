def find_optimal_location(N, grid):
    houses = []

    # 주택 좌표를 추출
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'H':
                houses.append((i, j))

    min_distance_sum = float('inf')
    best_location = (0, 0)

    # 각 지점에 대해 거리 합을 계산
    for i in range(N):
        for j in range(N):
            distance_sum = 0
            for (hx, hy) in houses:
                distance_sum += abs(hx - i) + abs(hy - j)
            # 최소 거리 합을 찾고 업데이트
            if distance_sum < min_distance_sum:
                min_distance_sum = distance_sum
                best_location = (i, j)
            elif distance_sum == min_distance_sum:
                if i < best_location[0] or (i == best_location[0] and j < best_location[1]):
                    best_location = (i, j)

    return best_location

# 입력 받기
N = int(input().strip())
grid = [input().strip() for _ in range(N)]

# 최적 위치 찾기
optimal_location = find_optimal_location(N, grid)

# 결과 출력
print(optimal_location[0] + 1, optimal_location[1] + 1)
