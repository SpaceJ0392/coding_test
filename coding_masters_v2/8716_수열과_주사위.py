def calculate_expected_value(K, n, paper_values):
    max_expected_value = -100

    for dice_sum in range(3, 19):  # Possible dice sum ranges from 3 to 18
        expected_value = 0
        for i in range(n):
            if K + dice_sum <= i + 1: break # If K + dice_sum exceeds N, score is -100
                
            expected_value += min(paper_values[i], 100)
        max_expected_value = max(max_expected_value, expected_value)

    return max_expected_value

def find_best_K(n, paper_values):
    max_expected_value = -100
    best_K = []

    for K in range(1, n + 1):
        expected_value = calculate_expected_value(K, n, paper_values)

        if expected_value >= max_expected_value:
            max_expected_value = expected_value
            best_K.append(K)

    return best_K


n = int(input())
paper_values = list(map(int, input().split()))

best_score, best_K = find_best_K(n, paper_values)
print(best_score, best_K, sep='\n')
