
from collections import deque


def get_day(n):
    queue = deque((0, 1))
    height_queue = deque([1, 1])
    
    now_height = 1
    while queue and now_height != n:
        day, now_height = queue.popleft()
        by_height = height_queue.popleft()
        y_height = height_queue[0]
        
        
        # case 1: 날이 맑았음
        queue.append((day + 1, now_height + y_height + by_height))
        height_queue.append(now_height + y_height + by_height)
        
        # case 2: 날이 흐림
        
        # case 3 : 폭풍우
    pass


t =  int(input())
for _ in range(t):
    n = int(input())
    print(get_day(n))