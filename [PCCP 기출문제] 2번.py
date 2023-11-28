def union(y, x, step, target_map, path):
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    for idx in range(len(dy)):
        next_step = (y + dy[idx], x + dx[idx])
        if next_step in target_map and next_step not in path:
            path.append(next_step)
            step += 1
            union(next_step[0], next_step[1], step, target_map, path)


def solution(land):
    answer = 0
    target_map = [
        (y, x) for y in range(len(land)) for x in range(len(land[y])) if land[y][x] == 1
    ]
    land_map = [[0] * len(land[0]) for _ in range(len(land))]

    path = []
    before_len = 0
    for y, x in target_map:
        if (y, x) not in path:
            path.append((y, x))
            union(y, x, 1, target_map, path)

            for y, x in path:
                if land_map[y][x] == 0:
                    land_map[y][x] = len(path) - before_len

            before_len = len(path)

    for x in range(len(land[0])):
        answer_list = set()
        for y in range(len(land)):
            if land_map[y][x] != 0:
                answer_list.add(land_map[y][x])

        answer = max(sum(answer_list), answer)

    return answer


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
