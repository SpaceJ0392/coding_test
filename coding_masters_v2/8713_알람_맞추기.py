hour, min = map(int, input().split(':'))
n = int(input())

time = hour * 60 + min
time += ((n - 1) * (n)) // 2

hour, min = str((time // 60) % 24), str(time % 60)


if len(hour) == 1 : hour = '0' + hour
if len(min) == 1 : min = '0' + min

print(f'{hour}:{min}')

        