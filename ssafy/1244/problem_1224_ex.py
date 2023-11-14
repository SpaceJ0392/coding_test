import sys
sys.stdin = open("input.txt", "r")

for t_c in range(1, int(input()) + 1):
    num, ret = input().split()
    ret = int(ret)

    now = {num}
    path = set()

    for _ in range(ret):
        while now: # TODO - while의 역할
            target = list(now.pop())
            for i in range(len(target) - 1):
                for j in range(i + 1, len(target)):
                    target[i], target[j] = target[j], target[i]
                    path.add(''.join(target))  # path 의 중복 제거
                    target[j], target[i] = target[i], target[j]
        now, path = path, now

    print(f"#{t_c} {max(list(map(int, now)))}")
