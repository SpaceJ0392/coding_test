a, b, c = map(int, input().split())
ans, turn = 0, 0
while turn < 10:
    turn += b / c * (a / b)
    ans += 1

print(ans)
