def is_valid_connection(N, M, K, log):
    def get_group(computer):
        if computer == 0:
            return 0
        return (computer - 1) // M + 1

    prev_group = get_group(log[0])
    
    for i in range(1, K):
        current_group = get_group(log[i])
        if prev_group != current_group:
            if log[i] != 0 and log[i-1] != 0:
                return "NO"
        prev_group = current_group
    
    return "YES"

# 입력 받기
N, M = map(int, input().strip().split())
K = int(input().strip())
log = list(map(int, input().strip().split()))

# 결과 출력
print(is_valid_connection(N, M, K, log))
