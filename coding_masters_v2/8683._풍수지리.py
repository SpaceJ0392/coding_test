n, m = map(int, input().split())
ground = [list(input()) for _ in range(n)]

def is_valid(sy, sx, ey, ex):
    symbol = ground[sy][sx]

    for y in range(sy, ey + 1):
        for x in range(sx , ex + 1):
            if symbol != ground[y][x]: return False
    
    return True

def get_max_area(sy, sx):
    return max([(ey - sy + 1) * (ex - sx + 1) \
                for ey in range(sy, n) for ex in range(sx, m) if is_valid(sy, sx, ey, ex)])

ans = []
for y in range(n):
    for x in range(m):
       ans.append(get_max_area(y, x))
       a = 1

print(max(ans))