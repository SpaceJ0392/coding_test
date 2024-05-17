n, m = map(int, input().split())
moves = [tuple(map(int, input().split())) for _ in range(m)]
target = int(input())

cups = [i for i in range(n + 1)]
for f, s in moves:
    cups[f], cups[s] = cups[s], cups[f]

print(cups.index(target))