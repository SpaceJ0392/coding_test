idx = int(input())

pattern, n = [9], 3
for i in range(1, 16):
    n += 2 ** i
    pattern.append(n ** 2)

print(pattern[idx - 1])