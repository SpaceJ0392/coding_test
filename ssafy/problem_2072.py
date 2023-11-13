T = int(input())

for test_case in range(1, T + 1):
    target_list = list(map(int, input().split()))
    print(f"#{test_case} {sum([x for x in target_list if x%2 != 0])}")

