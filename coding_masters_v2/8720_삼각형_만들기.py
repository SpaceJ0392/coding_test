n = int(input())
stick = sorted(list(map(int, input().split())), reverse=True)

while len(stick) > 3 and stick[0] > stick[1] + stick[2]: stick = stick[1:]
while len(stick) > 3 and stick[-1]  + stick[-2] < stick[0]: stick.pop()

print(len(stick))
