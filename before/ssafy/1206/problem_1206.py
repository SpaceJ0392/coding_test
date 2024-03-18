import sys
sys.stdin = open("input.txt", "r")

for test_case in range(10):
    len_of_list = int(input())
    maps = list(map(int, input().split()))

    cnt = 0
    for idx in range(2, len_of_list - 2):
        left_height = max(maps[idx-1], maps[idx-2])
        right_height = max(maps[idx+1], maps[idx+2])

        if maps[idx] - left_height <= 0 or maps[idx] - right_height <= 0:
            continue

        cnt += min(maps[idx] - left_height, maps[idx] - right_height)

    print(f"#{test_case} {cnt}")