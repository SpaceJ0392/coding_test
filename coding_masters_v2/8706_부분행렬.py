def is_submatrix_with_sum(matrix, N, M, X):
    # 모든 가능한 부분 행렬을 검사
    for top in range(N):
        for bottom in range(top, N):
            for left in range(M):
                for right in range(left, M):
                    submatrix_sum = 0
                    for i in range(top, bottom + 1):
                        for j in range(left, right + 1):
                            submatrix_sum += matrix[i][j]
                    if submatrix_sum == X:
                        return "YES"
    return "NO"

# 입력 처리
N, M, X = map(int, input().strip().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

# 결과 출력
print(is_submatrix_with_sum(matrix, N, M, X))
