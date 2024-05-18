from collections import deque

n, m = map(int, input().split())
r1 = deque(list(map(int, input().split())))
r2 = deque(list(map(int, input().split())))


def get_attacker(r1, r2, attacker):
    if r1 == r2:
        return attacker

    if r1 == 3 and r2 == 2:
        return 1
    elif r1 == 2 and r2 == 1:
        return 1
    elif r1 == 1 and r2 == 3:
        return 1
    else:
        return 2


attacker, flag = 0, True
for _ in range(n * m):
    t1, t2 = r1.popleft(), r2.popleft()
    attacker = get_attacker(t1, t2, attacker)
    r1.append(t1)
    r2.append(t2)

    if attacker == 0:
        continue

    if t1 == t2:
        flag = False
        break

print(0) if flag else print(attacker)
