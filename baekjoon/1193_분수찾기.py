n = int(input())

line_list = [0]
i = 1
while line_list[-1] < n and line_list[-1] <= 10000000:
    line_list.append(line_list[-1] + i)
    i += 1

line = len(line_list) - 1 # 자신의 줄
loc = n - line_list[-2] - 1 # 자신의 위치

temp = []
if line % 2 == 0:
    temp = [f'{i}/{(line + 1) - i}' for i in range(1, line + 1)]
else:
    temp = [f'{(line + 1) - i}/{i}' for i in range(1, line + 1)]

print(temp[loc])