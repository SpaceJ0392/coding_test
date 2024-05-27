def find_pairs(arr):
    product_map = {}
    
    n = len(arr)
    
    # 모든 가능한 두 쌍을 탐색하여 곱을 계산
    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            
            if product in product_map:
                # 이미 동일한 곱이 존재하면 인덱스 비교
                (x, y) = product_map[product]
                if x != i and x != j and y != i and y != j:
                    return "YES"
            else:
                product_map[product] = (i, j)
    
    return "NO"

# 입력 처리
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# 결과 출력
print(find_pairs(arr))
