hour, min = map(int, input().split(':'))
n = int(input())

for i in range(n):
    min += i
    if min >= 60:
        hour += 1
        min = min - 60
    if hour > 23: hour = 0

hour, min = str(hour), str(min)
if len(hour) == 1: hour = '0' + hour
if len(min) == 1: hour = '0' + min
print(f'{hour}:{min}')
        