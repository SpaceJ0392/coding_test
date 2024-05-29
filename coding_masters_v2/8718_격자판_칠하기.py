def is_valid_color(grid, x, y, color):
    # Check top neighbor
    if x > 0 and grid[x - 1][y] == color:
        return False
    # Check left neighbor
    if y > 0 and grid[x][y - 1] == color:
        return False
    return True

def count_colorings(N, M):
    # Initialize the grid with -1 indicating no color
    grid = [[-1] * M for _ in range(N)]
    colors = [0, 1, 2]  # Three colors
    total_count = 0

    def backtrack(x, y):
        if x == N:
            total_count += 1
            return
        if y == M:
            backtrack(x + 1, 0)
            return
        
        for color in colors:
            if is_valid_color(grid, x, y, color):
                grid[x][y] = color
                backtrack(x, y + 1)
                # grid[x][y] = -1

    backtrack(0, 0)
    return total_count


N, M = map(int, input().split())

result = count_colorings(N, M)
print(result)
