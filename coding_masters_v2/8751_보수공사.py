def get_min_tiles(N, K, M, rain_areas):
    """
    도로 관리에 필요한 최소 타일 개수를 계산하는 함수

    Args:
        N: 도로 크기
        K: 타일 부식 기준 횟수
        M: 관리 일수
        rain_areas: 비가 내리는 영역 정보

    Returns:
        필요한 최소 타일 개수
    """
    tile_counts = [[0] * N for _ in range(N)]  # 타일별 비 맞은 횟수

    # 각 날짜에 대해 비가 내리는 영역 처리
    for x1, y1, x2, y2 in rain_areas:
        for i in range(x1 - 1, x2):
            for j in range(y1 - 1, y2):
                tile_counts[i][j] += 1

    # 교체 필요한 타일 개수 계산
    replacements = 0
    for i in range(N):
        for j in range(N):
            replacements += tile_counts[i][j] // K

    return replacements

# 입력 받기
N = int(input())
K = int(input())
M = int(input())
rain_areas = [list(map(int, input().split())) for _ in range(M)]

# 최소 타일 개수 계산 및 출력
min_tiles = get_min_tiles(N, K, M, rain_areas)
print(min_tiles)
