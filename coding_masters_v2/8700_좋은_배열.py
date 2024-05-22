n = int(input())
target_list = input().replace(' ', '').strip()

flag = False
visited = []

for i, target in enumerate(target_list):
    if i not in visited:
        p = target_list.find(target, i + 1)
        
        if 0 < (p - i) and (p - i) != 1:
            j = set(target_list[i + 1 : p])
            q = set(target_list[p + 1:])
            
            if len(j & q) == 0: flag = True
            else: 
                flag = False
                break
                
        visited += [i, p]

print('YES') if flag else print('NO')
