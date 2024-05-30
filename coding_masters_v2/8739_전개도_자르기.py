# 10x10 격자에서 정육면체의 가능한 모든 전개도를 탐색하여 합의 최대값을 구하는 함수
def max_sum_of_cube(grid):
    # 정육면체 전개도 패턴을 정의
    patterns = [
        [(0, 0), (1, 0), (2, 0), (1, -1), (1, 1), (1, 2)], # 십자형
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)], # 일자형
        [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)], # ㄴ자형
        # 더 많은 패턴을 여기에 추가할 수 있습니다
    ]

    max_sum = 0
    n = len(grid)

    # 각 패턴에 대해 격자 내 모든 위치에서 적용해보기
    for pattern in patterns:
        for i in range(n):
            for j in range(n):
                current_sum = 0
                valid = True
                for dx, dy in pattern:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n:
                        current_sum += grid[x][y]
                    else:
                        valid = False
                        break
                if valid:
                    max_sum = max(max_sum, current_sum)
    return max_sum

# 10x10 격자를 입력받기
grid = []
for _ in range(10):
    grid.append(list(map(int, input().split())))

# 최대 합 출력
print(max_sum_of_cube(grid))
