from itertools import permutations
import math


def solution(numbers):
    answer = 0
    numbers_list = list(set(int("".join(num)) for num in permutations(numbers)))
    max_num = max(numbers_list)
    prime_list = [True] * (max_num + 1)

    for num in range(2, int(math.sqrt(max_num)) + 1):
        if prime_list[num] == True:
            for target_idx in range(2, max_num):
                if num * target_idx > max_num:
                    break
                prime_list[num * target_idx] = False

    for idx in numbers_list:
        if prime_list[idx] == True:
            answer += 1

    return answer


print((solution("011")))
