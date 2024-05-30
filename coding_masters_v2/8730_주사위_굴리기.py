def roll_dice(dice, direction):
    east, south, west, north, top, bottom = dice
    if direction == 1:  # East
        return [bottom, south, top, north, east, west]
    elif direction == 2:  # South
        return [east, bottom, west, top, south, north]
    elif direction == 3:  # West
        return [top, south, bottom, north, west, east]
    elif direction == 4:  # North
        return [east, top, west, bottom, north, south]

def main():
    W, H = map(int, input().split())
    X, Y = map(int, input().split())
    dice = list(map(int, input().split()))
    N = int(input())
    moves = list(map(int, input().split()))

    # Initialize the plane
    plane = [[0 for _ in range(W)] for _ in range(H)]
    plane[Y][X] = dice[-1]

    for move in moves:
        new_X, new_Y = X, Y

        if move == 1:  # East
            new_X = X + 1
        elif move == 2:  # South
            new_Y = Y + 1
        elif move == 3:  # West
            new_X = X - 1
        elif move == 4:  # North
            new_Y = Y - 1

        if 0 <= new_X < W and 0 <= new_Y < H:
            X, Y = new_X, new_Y

        dice = roll_dice(dice, move)
        plane[Y][X] = dice[-1]

    for row in plane:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
