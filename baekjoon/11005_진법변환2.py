n, b = map(int, input().split())
numeric ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = ''
while n >= b:
    res += numeric[n % b]
    n //= b

res += numeric[n % b]
print(res[::-1])
    