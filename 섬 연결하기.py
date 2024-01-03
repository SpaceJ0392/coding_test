def solution(n, costs):
    answer = 0

    parent = list(range(0, n))
    costs.sort(key=lambda x: x[2])

    def union(x, y):
        a = find(x)
        b = find(y)
        if a != b:
            parent[a] = b

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    for i1, i2, cost in costs:
        if find(i1) != find(i2):
            union(i1, i2)
            print(parent)
            answer += cost

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
