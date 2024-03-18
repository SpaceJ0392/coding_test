def solution(n, wires):
    ans = n
    # [wires[i + 1:] + wires[:i] for i in range(len(wires))] : 하나씩 빼고 순환 (즉, 한개만 타켓팅하고 나머지로 검증)
    for sub_set in (wires[i + 1:] + wires[:i] for i in range(len(wires))):
        start_set = set(sub_set[0])
        [
            start_set.update(connect_set) for connect_set in sub_set if set(connect_set) & start_set
            # start 지점하고, 연결된 모든 경로를 담는다.
        ]  # 집합 연산자 & : 교집합 연산 - 기존의 set에서 비교하여 없는 원소만 추가하는 형식이다.
        ans = min(ans, abs(2 * len(start_set) - n)) # len(start_set) - (n - len(start_set)) == 2 * len(start_set) - n
    return ans


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

"""
참고 : https://velog.io/@s2ul2/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level2-%EC%A0%84%EB%A0%A5%EB%A7%9D%EC%9D%84
-%EB%91%98%EB%A1%9C-%EB%82%98%EB%88%84%EA%B8%B0-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
