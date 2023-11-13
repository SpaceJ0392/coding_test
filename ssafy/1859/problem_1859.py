import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    len_of_list = int(input())
    target_list = list(map(int, input().split()))

    total_price = 0

    while len(target_list) != 0:
        max_idx, max_item = max(enumerate(target_list), key=lambda x: x[1])
        total_price += (max_item * max_idx) - sum(target_list[:max_idx])
        target_list = target_list[max_idx + 1:]

    print(f"#{test_case} {total_price}")
