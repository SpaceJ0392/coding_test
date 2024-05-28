from collections import deque
original = input()
target  = input()

flag = False
for _ in range(len(original)):
    target = target[1:] + target[0]
    if target == original:
        flag = True
        break

print('YES') if flag else print('NO')