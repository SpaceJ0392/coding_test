import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    num, ret = map(str, input().split())

    for i in range(int(ret)):

        if ret > len(num):
            ''.join(sorted(num))
            break


