n, k = map(int, input().split())
pivot = n // 2  if n % 2 == 0 else n // 2 + 1

ans = 0
if k <= pivot:
    ans = 2 * k - 1
else:
    k -= pivot
    ans = 2 * k

print(ans)