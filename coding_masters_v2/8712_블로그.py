n, k = map(int, input().split())
customers = list(map(int, input().split()))

max_avg, fast_day = -float('inf'), k + 1
for idx in range(len(customers) - k + 1):
    temp = [customers[idx + i] for i in range(k)]
    avg = sum(temp) / k
    if max_avg < avg:
        max_avg = avg
        fast_day = idx + 1

print(fast_day)