dist, train, fly = map(int, input().split())

train /= 3600
fly /= 3600

while dist != 0:
    dist -= (train * 2)
    