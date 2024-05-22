n = int(input())
target_list = input().replace(' ', '').strip()

flag = True
s_idx, b_idx = 0, 0
visited = []
while len(visited) != 2 * n:
    if s_idx not in visited:
        b_idx = target_list.find(target_list[s_idx], s_idx + 1)
    
    if b_idx == 2 * n - 1:
        break
    
    if b_idx - s_idx != 1:
        middle = set(target_list[s_idx + 1:b_idx])
        back = set(target_list[b_idx + 1:])
        
        if len(middle & back) != 0:
            flag = False
            break
    
    s_idx += 1
    visited += [s_idx, b_idx]

print('YES') if flag else print('NO')
