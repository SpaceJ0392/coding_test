def solution(answers):
    answer = []

    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    solve = [0, 0, 0]
    for i in range(len(answers)):
        if person1[i % 5] == answers[i]:
            solve[0] += 1
        if person2[i % 8] == answers[i]:
            solve[1] += 1
        if person3[i % 10] == answers[i]:
            solve[2] += 1

    for idx, val in enumerate(solve):
        if val == max(solve):
            answer.append(idx + 1)

    return answer


print(solution([1, 3, 2, 4, 2]))
