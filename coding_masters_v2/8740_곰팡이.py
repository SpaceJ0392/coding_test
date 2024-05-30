MOD = 1000000007

def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_pow(mat, exp):
    result = [[1, 0], [0, 1]] # Identity matrix
    base = mat
    
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exp //= 2
    
    return result

def total_mold_count(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, N)
    
    # T(N) is in result[0][0] as it represents F(N) in the transformation matrix
    return result[0][0]

# N 입력 받기
N = int(input().strip())

# N분 후의 총 곰팡이 수 출력
print(total_mold_count(N))
