from collections import Counter


def solution(picks, minerals):
    answer = 0
    minerals = sorted(
        [minerals[i : i + 5] for i in range(0, len(minerals), 5)],
        key=lambda x: (x.count("diamond"), x.count("iron")),
    )

    picks = list(reversed([(idx, pick) for idx, pick in enumerate(picks)]))
    pick_damaged = [
        {"diamond": 1, "iron": 1, "stone": 1},
        {"diamond": 5, "iron": 1, "stone": 1},
        {"diamond": 25, "iron": 5, "stone": 1},
    ]

    # 묶은 상태에서 정렬해서 dia가 가장 많은 거 부터 picks를 순차적으로 줄이면 문제 해결
    pick_type, pick_cnt = 0, 0
    while picks and minerals:

        while pick_cnt == 0:
            pick_type, pick_cnt = picks.pop()
        pick_cnt -= 1

        sub_minerals = minerals.pop()
        for mineral in sub_minerals:
            answer += pick_damaged[pick_type][mineral]

    return answer


print(
    solution(
        [0, 1, 1],
        [
            "diamond",
            "diamond",
            "diamond",
            "diamond",
            "diamond",
            "iron",
            "iron",
            "iron",
            "iron",
            "iron",
            "diamond",
        ],
    )
)
print(
    solution(
        [1, 3, 2],
        ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
    )
)
