n = int(input())
target_list = input().replace(' ', '').strip()

flag = True
for i in range(1, n + 1):
    s_idx = target_list.find(str(i))
    b_idx = target_list.find(str(i), s_idx + 1)
    
    if b_idx - s_idx != 1 and b_idx != 2 * n - 1:
        middle = set(target_list[s_idx + 1:b_idx])
        back = set(target_list[b_idx + 1:])
        
        if len(middle & back) != 0:
            flag = False
            break

print('YES') if flag else print('NO')
