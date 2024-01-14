answer = 0


def dfs(depth, numbers, target, tot):
    global answer

    if depth == len(numbers) and tot != target:
        return
    elif depth == len(numbers) and tot == target:
        answer += 1
        return

    dfs(depth + 1, numbers, target, tot + numbers[depth])
    dfs(depth + 1, numbers, target, tot - numbers[depth])


def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
