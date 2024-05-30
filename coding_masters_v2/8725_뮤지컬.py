def min_days_to_watch_all_actors(N, K, actors):
    from collections import defaultdict

    # 배우의 등장 횟수를 저장하는 딕셔너리
    count = defaultdict(int)
    unique_actors = 0
    start = 0
    min_days = N

    for end in range(N):
        # 현재 배우를 윈도우에 추가
        if count[actors[end]] == 0:
            unique_actors += 1
        count[actors[end]] += 1

        # 모든 배우가 포함되면 윈도우를 줄이기 시작
        while unique_actors == K:
            min_days = min(min_days, end - start + 1)
            count[actors[start]] -= 1
            if count[actors[start]] == 0:
                unique_actors -= 1
            start += 1

    return min_days

# 입력 받기
N, K = map(int, input().strip().split())
actors = list(map(int, input().strip().split()))

# 결과 출력
print(min_days_to_watch_all_actors(N, K, actors))
