from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while q1_sum != q2_sum:
        if q1_sum > q2_sum:
            queue2.append(queue1.popleft())
            answer += 1
        elif q1_sum < q2_sum:
            queue1.append(queue2.popleft())
            answer += 1

        q1_sum, q2_sum = sum(queue1), sum(queue2)
        if q1_sum == 0 or q2_sum == 0:
            answer = -1
            break

    return answer
