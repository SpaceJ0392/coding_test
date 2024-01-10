def solution(sequence, k):
    answer = []
    sub_sequence = []

    start, end = 0, 0
    while len(sequence) > end >= start:
        target = sequence[start : end + 1]
        target_sum = sum(sequence[start : end + 1])
        if sum(sequence[start : end + 1]) == k:
            sub_sequence.append([start, end])

        if sum(sequence[start : end + 1]) > k:
            end -= 1
            start = end
            continue

        end += 1

    print(sub_sequence)
    return answer


print(solution([1, 2, 3, 4, 5], 7))
