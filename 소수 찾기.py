from itertools import permutations


def solution(numbers):
    answer = 0
    permute_list = []
    for i in range(1, len(numbers) + 1):
        permute_list += [int("".join(num)) for num in permutations(numbers, i)]

    permute_set = set(permute_list)  # 중복 제거

    # 소수 구하기
    max_num = max(permute_set)
    for num in permute_set:
        for i in range(2, max_num + 1):
            if num % i == 0 and num != i:
                break
            if num % i == 0 and num == i:
                answer += 1

    return answer


print((solution("17")))
