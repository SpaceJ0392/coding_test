def solution(operations):
    queue = list()

    for oper in operations:
        if "I" in oper:
            order, target = oper.split()
            queue.append(int(target))
            queue.sort()
        if len(queue) != 0:
            if "D -1" == oper:
                queue.pop(0)
            if "D 1" == oper:
                queue.pop()

    if len(queue) != 0:
        return [queue.pop(), queue.pop(0)]
    else:
        return [0, 0]


print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)
