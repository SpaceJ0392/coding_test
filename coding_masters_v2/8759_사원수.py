def multiply_quaternions(a, b):
    """
    두 사원수를 곱하는 함수

    Args:
        a: 첫 번째 사원수 (a, b, c, d)
        b: 두 번째 사원수 (w, x, y, z)

    Returns:
        곱셈 결과 사원수 (o, p, q, r)
    """
    a1, b1, c1, d1 = a
    a2, b2, c2, d2 = b

    o = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
    p = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
    q = a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2
    r = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2

    return o, p, q, r

# 입력 받기
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

# 사원수 곱셈 계산
result = multiply_quaternions(a, b)

# 결과 출력
print(*result)  # 언패킹하여 공백으로 구분하여 출력
