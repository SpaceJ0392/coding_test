n = int(input())
target_list = input().replace(' ', '')

flag = True
for i in range(1, n + 1):
    s_idx = target_list.find(str(i))
    b_idx = target_list.find(str(i), s_idx + 1)
    if b_idx - s_idx != 1 and b_idx != n - 1:
        middle = set(target for target in list(target_list[s_idx + 1:b_idx]))
        back = set(target for target in list(target_list[b_idx + 1:]))

        if len(middle.intersection(back)) != 0:
            flag = False
            break

print('YES') if flag else print('NO')
