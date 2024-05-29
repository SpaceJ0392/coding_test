import itertools
import sys

N = int(input())
paper = list(map(int, input().split()))


def calculate_dice_probabilities():
    probabilities = {i: 0 for i in range(3, 19)}

    for combination in itertools.product(range(1, 7), repeat=3):
        probabilities[sum(combination)] += 1
    
    return probabilities

def calculate_expected_scores(N, paper):
    dice_probabilities = calculate_dice_probabilities()
    expected_scores = []
    
    for K in range(1, N + 1):
        expected_value = 0
        for dice_sum in range(3, 19):
            if K + dice_sum <= N:
                expected_value += paper[K + dice_sum - 1] * dice_probabilities[dice_sum]
            else:
                expected_value += -100 * dice_probabilities[dice_sum]
        expected_scores.append((expected_value, K))
    
    return expected_scores


expected_scores = calculate_expected_scores(N, paper)

max_expected_value = max(expected_scores)[0]
optimal_K_values = sorted([K for (value, K) in expected_scores if value == max_expected_value])

# 216을 곱해서 출력
print(int(max_expected_value))
print(' '.join(map(str, optimal_K_values)))
