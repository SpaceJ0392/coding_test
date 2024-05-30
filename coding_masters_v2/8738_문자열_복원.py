incoding = input()

alphabet = {i : chr(ord('a') - 1 + i) for i in range(1, ord('z') - ord('a') + 2)}
now = 0
ans = ''
while now < len(incoding) or now != -1:
    idx = incoding.find('0', now)
    if idx != len(incoding) - 1 and incoding[idx + 1] == '0': idx += 1
    if idx == -1: break
    
    for i in range(now, idx - 2): ans += alphabet[int(incoding[i])]
    ans += alphabet[int(incoding[idx-2:idx])]
    
    now = idx + 1

for i in range(now, len(incoding)): ans += alphabet[int(incoding[i])]

print(ans)