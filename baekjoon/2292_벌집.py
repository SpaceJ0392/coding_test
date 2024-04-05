n = int(input())
pattern = [1]

i = 1
while pattern[-1] < n and pattern[-1] <= 1000000000:
    pattern.append(pattern[-1] + (6 * i))
    i += 1

print(len(pattern))
