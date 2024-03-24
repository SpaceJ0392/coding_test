p, q = map(int, input().split())
n = int(input())

num = []
for _ in range(n + 1):
    p *= 10
    temp_q = q
    for i in range(1, 10):
        temp_q = q * i
        
        if p <= temp_q: 
            num.append(str(i - 1))
            temp_q = q * (i - 1)
            break
        
        if i == 9: num.append(str(i))

    p -= temp_q

# TODO - 올림 처리
# 올리는 숫자가 9면, 그 앞이 1 증가 해야함
# 그런데, 그 앞도 9면, 계속해서 그 앞이 1씩 증가 (9가 아닐때 까지)
if num[-1] > '5':
    last_idx = len(num) - 2
    
    while num[last_idx] == '9':
        num[last_idx] = '0'
        last_idx -= 1
    
    num[last_idx] = str(int(num[last_idx]) + 1)

print('0.' + ''.join(num[:-1]))


