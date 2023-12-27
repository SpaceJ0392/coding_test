def solution(people, limit):
    answer = 0
    boat = 0
    people = sorted(people, reverse=True)

    while people:
        while people and people[-1] + boat <= limit:
            boat += people[-1]
            people.pop()

        answer += 1
        boat = 0

    return answer


print(solution([70, 80, 50, 50], 100))
