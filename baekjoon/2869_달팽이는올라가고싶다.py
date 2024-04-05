up, down, height = map(int, input().split())

if height % (up - down) == 0:
    print(height - down)
else:
    print(height // (up - down) + 1)