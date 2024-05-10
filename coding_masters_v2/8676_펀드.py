base, credit = map(int, input().split())
n, m = map(int, input().split())
prices = sum(sorted([int(input()) for _ in range(n)], reverse=True)[:m])

print(base + (credit * prices))