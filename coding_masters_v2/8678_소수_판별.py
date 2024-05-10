import math
n = int(input())
flag = False
if n >= 2: 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = True
            break
  
    print(0) if flag else print(1)
    
else:
    print(0)