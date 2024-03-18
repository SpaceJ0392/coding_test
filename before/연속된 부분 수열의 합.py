def solution(seq, k):
    answer = []
    start, end, total = 0, 0, seq[0]
    seq += [0]
    min_length = len(seq)

    while end < len(seq) - 1:
        if total <= k:
            if total == k and end - start + 1 < min_length:
                answer = [start, end]
                min_length = end - start + 1
            end += 1
            total += seq[end]
        else:
            start += 1
            total -= seq[start - 1]

    return answer


print(solution([1, 2, 3, 4, 5], 7))
print(solution([2, 2, 2, 2, 2], 6))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
