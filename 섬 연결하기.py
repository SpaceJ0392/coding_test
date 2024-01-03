parent = list(range(0, 101))


def find(x):
    if parent[x] != x:
        find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    print(costs)
    for island1, island2, cost in costs:
        parent1 = find(island1)
        parent2 = find(island2)

        if parent1 != parent2:
            union(island1, island2)
            answer += cost

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
