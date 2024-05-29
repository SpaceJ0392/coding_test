def next_permutation(seq, n):
    i = n - 1
    while i > 0 and seq[i - 1] > seq[i]: i -= 1
    if i <= 0: return sorted(seq)
    
    # 2. 위치를 교환할 수 찾기
    j = n - 1
    while seq[j] < seq[i - 1]: j -= 1
        
    # 3. 두 수 교환
    seq[i - 1], seq[j] = seq[j], seq[i - 1]
    return seq[:i] + seq[i:][::-1]

def get_kth_permutation(N, K, permutation):
    for _ in range(K): 
        permutation = next_permutation(permutation, N)
    return permutation


N, K = map(int, input().split())
permutation = list(map(int, input().split()))

result = get_kth_permutation(N, K, permutation)
print(' '.join(map(str, result)))
