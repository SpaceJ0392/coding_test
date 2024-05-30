def prime_factors(p):
    factors = {}
    d = 2
    while d * d <= p:
        while (p % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            p //= d
        d += 1
    if p > 1:
        factors[p] = 1
    return factors

def count_factors_in_factorial(n, prime):
    count = 0
    power = prime
    while power <= n:
        count += n // power
        power *= prime
    return count

def trailing_zeros_in_base_p(n, p):
    factors = prime_factors(p)
    min_zeros = float('inf')
    
    for prime, exp in factors.items():
        count = count_factors_in_factorial(n, prime)
        min_zeros = min(min_zeros, count // exp)
    
    return min_zeros

# 입력 받기
p, n = map(int, input().split())

# 결과 출력
print(trailing_zeros_in_base_p(n, p))
