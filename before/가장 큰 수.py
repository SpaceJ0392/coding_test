def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))