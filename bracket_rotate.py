# def solution(s):
#     answer = -1
#     # 획인
#     # - 조건1 : 닫힌 괄호는 무조건 열리는 괄호보다 뒤에 있어야 한다. (아니면 X)
#
#     # 등장하는 열린 괄호의 위치 찾기
#     input_idx = [s.find(target) for target in "[{("]
#
#     # 등장하는 닫힌 괄호의 위치 찾기
#     closed_idx = []
#     for idx, target in enumerate("]})"):
#         target_idx = s.find(target)
#
#         if target_idx == -1 or target_idx <= input_idx[idx]:
#             answer = 0
#             break
#
#         closed_idx.append(target_idx)
#
#     # - 조건2 : 괄호 안에 괄호가 존재한다면, 안의 괄호는 무조건 열린 괄호와 닫힌 괄호 한 쌍이
#     #          존재해야 한다.
#     for idx in range(len(input_idx)):
#         if closed_idx[idx] - input_idx[idx] == 1:
#             continue
#         else:
#             pass
#     # 조건이 하나라도 성립하지 않으면 회전
#     # 회전
#
#     return answer


# def solution(s):
#     answer = -1
#
#     pattern = "[{(]})"
#     start_idx = 0
#     end_idx = len(s)
#
#     for _ in range(len(s)):
#         for idx in range(3):
#             input_idx = s.find(pattern[idx], start_idx, end_idx)
#             temp = s[input_idx:end_idx]
#             closed_idx = s.find(pattern[idx + 3], input_idx, end_idx)
#             closed_idx += input_idx
#
#             print(pattern[idx], " ", pattern[idx + 3], " ", input_idx, " ", closed_idx)
#             if input_idx >= closed_idx:
#                 answer = 0
#                 break
#
#             answer += 1
#
#     return answer


def is_valid(s):
    stack = []

    for target in s:
        if target in "[{(":
            stack.append(target)

        if target in "]})":
            if len(stack) == 0:
                return False

            item = stack.pop()
            if not((item == "[" and target == "]") or (item == "{" and target == "}")\
                    or (item == "(" and target == ")")):
                return False

    return len(stack) == 0


def solution(s):
    answer = 0

    for _ in range(len(s)):
        if is_valid(s):
            answer += 1

        s = s[1:] + s[0]

    return answer


print(solution("}]()[{"))
