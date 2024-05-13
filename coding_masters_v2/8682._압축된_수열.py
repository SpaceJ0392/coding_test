n, m = map(int, input().split())
targets = list(map(int, input().split()))

num = {}
for i in range(0, 62):
    if i < 10: num[i] = i
    elif i < 36: num[i] = chr(i + ord('A') - 10)
    else : num[i] = chr(i + ord('a') - 36)

def get_digits(i, target):
    if target < i or i == 10: return str(target)

    temp = ''
    while target:
        temp += str(num[target % i])
        target //= i

    return temp[::-1]

flag = True
for i in range(10, 63):
    targets_length = ''
    for target in targets:
        targets_length += get_digits(i, target)
        targets_length += ' '
    
    if len(targets_length) - 1 <= m:
        print(i)
        flag =False
        break

if flag: print(-1)