import math
play, good = map(int, input().split())
now_score = math.floor((good / play) * 100) / 100

n, score = 0, now_score
while now_score == score:
    score = math.floor(((good + n) / (play + n)) * 100) / 100
    n += 1

print(n - 1)