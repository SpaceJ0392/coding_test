from collections import deque

n = int(input())
path = deque([input() for _ in range(n)])

def dfs(path, target):
    if len(path) == 0:
        if ''.join(target)[::-1] == target:
            return True
        return False
    
    temp = path.pop()
    target.append(temp)
    dfs(path, target)
    path.appendleft(target.pop())

dfs(path, [])