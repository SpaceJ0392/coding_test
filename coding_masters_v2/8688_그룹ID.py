# 1개 에러...

# n, m = map(int, input().split())
# parents = [i + 1 for i in range(n)]
# cnt = [0] * n


# def find_parents(child):
#     if parents[child - 1] == child:
#         return child
#     else:
#         return find_parents(parents[child - 1])


# def union(n1, n2):
#     p1, p2 = find_parents(n1), find_parents(n2)
#     if p1 == p2:
#         return

#     if p1 < p2:
#         parents[p2 - 1] = p1
#         cnt[p1 - 1] += 1
#     else:
#         parents[p1 - 1] = p2
#         cnt[p2 - 1] += 1


# inputs = sorted([tuple(map(int, input().split())) for _ in range(m)])

# for n1, n2 in inputs:
#     union(n1, n2)

# print(cnt.index(max(cnt)) + 1)


# dfs 로 해결
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x1, x2 = map(int, input().split())
    graph[x1][x2] = 1
    graph[x2][x1] = 1

path = [[0] * (n + 1) for _ in range(n + 1)]
max_idx, max_lev = 0, 0


def dfs(now, lev, idx):
    global max_idx, max_lev

    if max_lev < lev:
        max_idx = idx
        max_lev = lev

    for x in range(len(graph[now])):
        if graph[now][x] == 1 and path[now][x] == 0:
            path[now][x] = 1
            dfs(x, lev + 1, idx)


for start in range(1, n + 1):
    dfs(start, 0, start)

print(max_idx)
