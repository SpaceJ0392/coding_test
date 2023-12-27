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


def other_solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


print(other_solution("4177252841", 9))
