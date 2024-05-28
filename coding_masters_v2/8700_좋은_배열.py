n = int(input())
target_list = input().replace(' ', '').strip()

flag = True
visited = []

for i, target in enumerate(target_list):
    if i not in visited:
        p = target_list.find(target, i + 1)
        visited += [i, p]
        if p == -1 or 0 > (p - i) or (p - i) == 1 or p == (2 * n - 1) : continue
        
        j = set(target_list[i + 1 : p])
        q = set(target_list[p + 1:])
        
        if len(j & q) != 0 and j & q != set():
            flag = False
            break

print('YES') if flag else print('NO')