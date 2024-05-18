paint = [list(input()) for _ in range(4)]

filter = [(1, 1), (0, 1), (1, 0)]

flag = False
for y in range(3):
    for x in range(3):
        cnt = 0
        for dy, dx in filter:
            if 0 <= y + dy < 4 and 0 <= x + dx < 4 and paint[y + dy][x + dx] == 'X':
                cnt += 1

        if cnt >= 3:
            flag = True
            break

print('yes') if flag else print('no')
