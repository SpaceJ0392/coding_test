x, y, z = map(int, input().split())


def is_valid(x, y, z):
    if x == z and x >= y:
        return True
    elif x == y and x >= z:
        return True
    elif y == z and y >= x:
        return True

    return False


print('possible') if is_valid(x, y, z) else print('impossible')
