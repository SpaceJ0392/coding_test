import sys
sys.stdin = open("input.txt", "r")

def dfs(depth):
    global answer
    if depth == ret:
        answer = max(answer, int(''.join(map(str, target))))
        return

    for now in range(len(target) - 1):
        for i in range(now + 1, len(target)):
            if target[now] <= target[i]:
                target[now], target[i] = target[i], target[now]

                # check_path = int("".join(map(str, target))) * 10 + depth
                # if check_path not in path:
                dfs(depth + 1)
                    # path.append(check_path)

                target[now], target[i] = target[i], target[now]


for test_case in range(1, int(input()) + 1):

    target, ret = list(input().split())
    ret = int(ret)
    target = list(map(int, target))

    answer = 0
    path = []
    dfs(0)

    print(f"#{test_case} {answer}")