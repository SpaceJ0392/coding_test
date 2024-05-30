from datetime import datetime, timedelta

def is_palindrome_time(time_str):
    return time_str == time_str[::-1]

def count_palindrome_times(t, k):
    # 초기 시각을 datetime 객체로 변환
    current_time = datetime.strptime(t, "%H:%M")
    k_delta = timedelta(minutes=k)
    
    seen_times = set()
    palindrome_count = 0

    for _ in range(1440):  # 24시간(1440분) 동안 모든 분을 체크
        time_str = current_time.strftime("%H:%M")
        if time_str in seen_times:
            break
        seen_times.add(time_str)

        # HH:MM 형식의 시간 문자열이 팰린드롬인지 확인
        if is_palindrome_time(time_str.replace(":", "")):
            palindrome_count += 1

        # 시간을 k분 증가
        current_time += k_delta

    return palindrome_count

# 입력 받기
initial_time = input().strip()
k = int(input().strip())

# 결과 출력
result = count_palindrome_times(initial_time, k)
print(result)
