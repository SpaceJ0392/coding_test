input_code = input()[1:]
temp = [tuple(input_code[:2]), tuple(input_code[2:4]), tuple(input_code[4:])]

to_dec = {}
for i in range(0, 16):
    if i < 10: to_dec[i] = i
    else: to_dec[chr(ord('A') + i - 10)] = i


for idx, item in enumerate(temp):

     


def change_digit(n, digit):
    data = ''
    while n >= digit:
        data += str(n % digit)
        n //= digit
    
    return data.reverse()

