n, b = input().split()
n = n[::-1]
num_dict = {chr(ascii) : ascii - ord('A') + 10 for ascii in range(ord('A'), ord('Z') + 1)}

res = 0
for i in range(len(n)):
    if num_dict.get(n[i]) == None:
        res += (int(n[i]) * int(b) ** i)
    else:
        res += (num_dict[n[i]] * int(b) ** i)

print(res)