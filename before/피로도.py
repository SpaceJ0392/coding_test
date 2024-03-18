path = []
max_depth = 0

def dfs(depth, k, dungeons):
    global max_depth

    if depth == len(dungeons):
        return

    for dungeon in dungeons:
        if dungeon[0] <= k and dungeon not in path:
            path.append(dungeon)
            max_depth = max(max_depth, depth + 1)
            dfs(depth + 1, k - dungeon[1], dungeons)
            path.pop()


def solution(k, dungeons):
    dfs(0, k, dungeons)
    return max_depth


print('max_depth : ' ,solution(80, [[80, 20], [50, 40], [30, 10]]))
