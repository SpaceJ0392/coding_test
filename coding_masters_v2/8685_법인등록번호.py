front = list(input())
back = list(input())
error = int(input())

ans = list('XXXXX')

a = sum([int(n) for idx, n in enumerate(front, 1) if idx % 2 != 0] +
        [int(n) for idx, n in enumerate(back, 1) if idx % 2 != 0])
b = sum([int(n) for idx, n in enumerate(front, 1) if idx % 2 == 0] +
        [int(n) for idx, n in enumerate(back, 1) if idx % 2 == 0])

if error == 0:
    r = 0
else:
    r = (10 - error)

loss_nums = [int(str(x) + str(y)) for x in range(1, 10)
             for y in range(10) if (x + a + (2 * y) + (2 * b)) % 10 == r]

for loss in loss_nums:
    if 11 <= loss <= 15:
        ans[0] = 'O'
    elif 21 <= loss <= 22:
        ans[1] = 'O'
    elif 31 <= loss <= 51:
        ans[2] = 'O'
    elif 81 <= loss <= 86:
        ans[3] = 'O'
    elif loss == 71:
        ans[4] = 'O'

print(*ans, sep='')
