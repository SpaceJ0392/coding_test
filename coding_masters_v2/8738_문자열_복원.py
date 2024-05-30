def decode_string(encoded):
    i = 0
    decoded_chars = []
    
    while i < len(encoded):
        # Check if the current and next characters form a number >= 10
        if i + 2 <= len(encoded) and encoded[i + 1] == '0':
            # Extract the two-digit number
            number = int(encoded[i:i + 2])
            decoded_chars.append(chr(ord('a') + number - 1))
            i += 3  # Move past the two digits and the trailing '0'
        else:
            # Extract the single digit number
            number = int(encoded[i])
            decoded_chars.append(chr(ord('a') + number - 1))
            i += 1  # Move past the single digit
    
    return ''.join(decoded_chars)

# 입력 받기
encoded_string = input().strip()

# 결과 출력
decoded_string = decode_string(encoded_string)
print(decoded_string)
