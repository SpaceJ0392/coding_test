def solution(people, limit):
    answer = 0
    boat = 0
    people = sorted(people, reverse=True)

    while people:

        p_weight = people[-1]
        while p_weight + boat <= limit and len(people) > 1:
            boat += people.pop()
            p_weight = people[-1]

        answer += 1
        boat = 0

        if len(people) == 1:
            break

    return answer + 1


print(solution([70, 80, 50, 50], 100))
