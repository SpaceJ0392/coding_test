from collections import deque


def solution(plans):
    answer = []

    temp = []
    for homework, start, playtime in plans:
        start = start.split(":")
        start = int(start[0]) * 60 + int(start[1])
        temp.append([homework, start, int(playtime)])
    plans_q = deque(sorted(temp, key=lambda x: x[1]))
    last_q = deque()
    print(plans_q)

    before = plans_q.popleft()
    before_end = before[1] + before[2]
    while plans_q:
        now = plans_q.popleft()
        if now[1] < before_end:
            before[2] = before_end - now[1]
            last_q.append(before)
        else:
            answer.append(before[0])

            while before_end < now[1] and last_q:
                before = last_q.pop()
                if before[2] - (now[1] - before_end) <= 0:
                    answer.append(before[0])
                    before_end += before[2]
                else:
                    before[2] -= (now[1] - before_end)
                    before_end += (now[1] - before_end)
                    last_q.append(before)

        before = now
        before_end = now[1] + now[2]

        # 마지막 값
        if len(plans_q) == 0: answer.append(before[0])

    while last_q:
        answer.append(last_q.pop()[0])

    return answer


print(
    solution(
        [
            ["science", "12:40", "50"],
            ["music", "12:20", "40"],
            ["history", "14:00", "30"],
            ["computer", "12:30", "100"],
        ]
    )
)

print(
    solution(
        [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
    )
)


def other_solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))


print(
    other_solution(
        [
            ["science", "12:40", "50"],
            ["music", "12:20", "40"],
            ["history", "14:00", "30"],
            ["computer", "12:30", "100"],
        ]
    )
)