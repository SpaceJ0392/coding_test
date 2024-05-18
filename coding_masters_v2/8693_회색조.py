input_code = input()[1:]


def to_dec(hex_code):
    dec_list = {}
    for i in range(16):
        if i < 10:
            dec_list[str(i)] = i
        else:
            dec_list[chr(ord('A') + i - 10)] = i

    result = 0
    for code, i in zip(hex_code, range(16, 0, -15)):
        result += dec_list[code] * i

    return result


dec_list = [to_dec(input_code[i: i + 2]) for i in range(0, 6, 2)]
dec_avg = round(sum(dec_list) / len(dec_list))


def to_hex(dec_code):
    hex_list = {}
    for i in range(16):
        if i < 10:
            hex_list[i] = str(i)
        else:
            hex_list[i] = chr(ord('A') + i - 10)

    hex_code = ''
    if dec_code >= 16:
        while dec_code >= 16:
            hex_code += hex_list[dec_code % 16]
            dec_code //= 16

        hex_code += hex_list[dec_code]
    else:
        hex_code += hex_list[dec_code] + '0'

    return hex_code[::-1]


hex_avg = to_hex(dec_avg)
print(f'#{hex_avg * 3}')
