def solution(queue1, queue2):
    answer = 0

    while sum(queue1) != sum(queue2) and len(queue1) != 0 and len(queue2) != 0:
        queue2.append(queue1.pop(0))
        answer += 1

        print(sum(queue1), sum(queue2))

        if len(queue1) == 0 or len(queue2) == 0:
            answer = -1
            break

        if sum(queue1) == sum(queue2):
            break

        queue1.append(queue2.pop(0))
        answer += 1

        print(sum(queue1), sum(queue2))

    return answer


solution([1, 2, 1, 2], [1, 10, 1, 2])
