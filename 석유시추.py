from collections import Counter


def solution(land):
    answer = 0
    parent = dict()

    # 부모 초기화
    for y in range(len(land)):
        for x in range(len(land[y])):
            if land[y][x] == 1:
                parent[(y, x)] = (y, x)

    def union(p1, p2):
        if parent[p1] != parent[p2]:
            parent[p2] = parent[p1]

    # Union
    ny = [0, 1]
    nx = [1, 0]
    for y, x in parent:
        for i in range(len(ny)):
            if parent.get((y + ny[i], x + nx[i])) is not None:
                union((y, x), (y + ny[i], x + nx[i]))

    # Counting
    oil_amount = Counter(parent.values())

    # 탐색
    for x in range(0, len(land[0])):
        entered = set()
        for y in range(0, len(land)):
            if land[y][x] == 1:
                entered.add(parent[(y, x)])

        tot = 0
        for target in entered:
            tot += oil_amount[target]

        answer = max(answer, tot)

    return answer


print(
    solution(
        [
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1],
        ]
    )
)
print(
    solution(
        [
            [1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
        ]
    )
)


