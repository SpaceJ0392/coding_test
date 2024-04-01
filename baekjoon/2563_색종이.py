n = int(input())

square = []
for _ in range(n):
    x, y = map(int, input().split()) 
    square.append([x, y, x + 10, y + 10])

for idx, target in enumerate(square):
    target_x, target_y, target_max_x, target_max_y = target
    for sq in square[idx+1:]:
        pass
