from collections import deque


end, start = map(int, input().split())

while start < end:
     if abs(start * 2 - end) > abs(start + 1 - end): start *= 2 
     else: start += 1
     
    