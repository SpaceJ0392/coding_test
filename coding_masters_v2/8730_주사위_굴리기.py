W, H = map(int, input().split())
X, Y = map(int, input().split())
plane = [[0] * W for _ in range(H)]

dice = list(map(int, input().split()))
steps = int(input())
path = list(map(int, input().split()))

def turn(dir, dice):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, b, f, d, c, a
    elif dir == 2: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, e, c, f, d, b
    elif dir == 3: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = f, b, e, d, a, c
    else: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, f, c, e, b, d
    
    return dice

plane[Y][X] = dice[-1]
direction = {1:(0,1), 2:(1,0), 3:(0,-1), 4:(-1,0)}
for step in path:
    dy, dx = direction[step]
    ny, nx = Y + dy, X + dx
    dice = turn(step, dice)
    if ny >= H or ny < 0 or nx >= W or nx < 0:
        plane[Y][X] = dice[-1]
    else:
        plane[ny][nx] = dice[-1]
        Y, X = ny, nx

for line in plane: print(*line)