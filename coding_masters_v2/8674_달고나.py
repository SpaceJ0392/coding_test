cols, rows = map(int, input().split())
field = [list(input()) for _ in range(cols)]

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
checked = [[0] * rows for _ in range(cols)]
cnt = 0
for y in range(cols):
    for x in range(rows):
            if 0 <= y + dy < cols and 0 <= x + dx < rows and field[y + dy][x + dx] == '1': continue
            checked[y][x] = 1
            checked[y + dy][x + dx] = 1

print(cnt)