def solution(number, k):
    answer = ""
    cnt = 0

    while cnt < k:
        lost_num = min(list(number[:k]))
        number = number.replace(lost_num, "", 1)
        # print(number)
        cnt += 1

    return number


print(solution("1234567890123456789012345678901234567890", 1))
print(solution("4177252841", 9))
