def solution(priorities, location):
    answer = 0
    priorities = list(enumerate(priorities))

    while len(priorities) != 0:
        max_val = max(priorities, key=lambda x: x[1])
        start_idx = priorities.index(max_val)
        answer += 1

        priorities = priorities[start_idx:] + priorities[:start_idx]

        if location == priorities[0][0]:
            break

        priorities.pop(0)

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
