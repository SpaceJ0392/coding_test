def solution(number, k):
    answer = ""
    sorting_num = sorted(set(number))
    target_num = sorting_num[:k]

    cnt = 0
    for letter_idx in range(len(number)):
        if cnt >= k:
            answer += number[letter_idx:]
            break

        if number[letter_idx] in target_num:
            cnt += 1
            continue

        answer += number[letter_idx]
    return answer


# print(solution("1924", 2))
print(solution("1231234", 3))
