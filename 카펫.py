def solution(brown, yellow):
    answer = []
    xy = brown + yellow
    x_plus_y = (brown + 4) // 2

    for y in range(1, xy // 2 + 1):
        x = xy / y
        if x + y == x_plus_y:
            answer = [x, y]
            break

    return answer


print(solution(24, 24))
