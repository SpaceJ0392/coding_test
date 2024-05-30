import math
price = int(input())
tax = int(price / 110 * 10)

print(-1) if tax < 10 else print(price - tax, tax)
