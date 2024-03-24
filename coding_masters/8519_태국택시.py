'''
input
4 5
1 3 10
2 3 20
4 1 30
3 4 40
2 4 50

6 5
1 3 10
4 2 20
5 3 30
6 1 40
6 4 20
'''
town, texi = map(int, input().split())
texi_costs = [list(map(int, input().split())) for _ in range(texi)]
texi_costs.sort(key=lambda x : (x[2], x[0]))

town_path = [0] * (town + 1)
tot_cost = 0
for t1, t2, cost in texi_costs:
    if town_path[t1] == 1 and town_path[t2] == 1: continue
    if town_path.count(1) == len(town_path) - 1: break
    town_path[t1], town_path[t2] = 1, 1
    tot_cost += cost

print(tot_cost)
    
