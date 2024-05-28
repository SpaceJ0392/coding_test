# n, k = map(int, input().split())
# home = list(map(int,input().split()))

# max_sum, max_now = 0, 0
# for now in range(max(home)):
#     left, right = now - k, now + k
#     if now - k < 0: left = 0
    
#     temp_sum = 0
#     for now_home in home:
#         dist = abs(now - now_home)
#         if dist <= k: temp_sum += dist
#         else: temp_sum -= dist
    
#     if max_sum < temp_sum:
#         max_sum = temp_sum
#         max_now = now

# print(max_sum, max_now)

def calculate_satisfaction(house_positions, K, location):
    satisfaction = 0
    for house in house_positions:
        distance = abs(house - location)
        if distance <= K:
            satisfaction += distance
        else:
            satisfaction -= distance
    return satisfaction

def find_best_location(N, K, house_positions):
    house_positions.sort()
    max_satisfaction = float('-inf')
    best_location = None
    
    for location in house_positions:
        current_satisfaction = calculate_satisfaction(house_positions, K, location)
        if current_satisfaction > max_satisfaction:
            max_satisfaction = current_satisfaction
            best_location = location
        elif current_satisfaction == max_satisfaction:
            best_location = min(best_location, location)
    
    return best_location

# 입력 받기
N, K = map(int, input().split())
house_positions = list(map(int, input().split()))

# 최적의 위치 찾기
best_location = find_best_location(N, K, house_positions)

# 결과 출력
print(best_location)
