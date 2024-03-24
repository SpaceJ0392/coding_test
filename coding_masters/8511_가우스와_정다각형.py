n = int(input())
fermat_prime = [65537, 257, 17, 5, 3]

flag = False
for prime_num in fermat_prime:
    if n >= prime_num and (n / prime_num).is_integer():
        n //= prime_num
    if n == 1: flag == True

square_2, target = [1, 2], 2
while True:
    target *= 2
        
    if target >= 10 ** 8: break
    square_2.append(target)
        
if n in square_2: flag = True
    
if flag:
    print('YES')
else:
    print('NO')
