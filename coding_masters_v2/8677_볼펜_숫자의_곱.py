n = int(input())
pens = sorted(list(map(int, input().split())), reverse=True)
max_price = -float('inf')

path = [False] * n
def dfs(pens, lev, now, price):
    global max_price
    if lev == now:
        if max_price < price: max_price = price
        return
    
    for i, pen in enumerate(pens):
        if path[i] == True: continue
        path[i] = True
        dfs(pens, lev, now + 1, price * pen)
        path[i] = False

dfs(pens, 2, 0, 1)
dfs(pens, 3, 0, 1)
print(max_price)
