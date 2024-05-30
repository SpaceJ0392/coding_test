def count_trailing_zeros(x):
    count = 0
    power_of_5 = 5
    while x >= power_of_5:
        count += x // power_of_5
        power_of_5 *= 5
    return count

def find_minimum_x(n):
    low, high = 0, 5 * n
    while low < high:
        mid = (low + high) // 2
        if count_trailing_zeros(mid) < n:
            low = mid + 1
        else:
            high = mid
    return low

# 입력 받기
n = int(input())

# 결과 출력
print(find_minimum_x(n))
