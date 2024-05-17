n = int(input())
move = [tuple(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(len(move) - 1): 
    y, x = move[i]
    ny, nx = move[i+1]
    
    if y == ny and nx - x > 0: ans.append((2, nx - x))
    elif y == ny and nx - x < 0: ans.append((4, x - nx))
    elif nx == x and ny - y > 0: ans.append((1, ny - y))
    else: ans.append((3, y - ny))

for dir, dist in ans: print(dir, dist)
