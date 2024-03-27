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
town, taxi = map(int, input().split())
taxi_costs = [list(map(int, input().split())) for _ in range(taxi)]
taxi_costs.sort(key=lambda x : (x[2], x[0]))

town_path = list(range(town + 1))

def find_parent(child):
    if town_path[child] == child:
        return town_path[child]
    else:
        return find_parent(town_path[child])

def union(child1, child2):
    p1 = find_parent(child1)
    p2 = find_parent(child2)
    if p1 >= p2:
        town_path[p1] = p2
    else:
        town_path[p2] = p1

tot_cost = 0
for t1, t2, cost in taxi_costs:
    if find_parent(t1) == find_parent(t2): continue
    if town_path.count(town_path[1]) == town: break
    union(t1, t2)
    tot_cost += cost

print(tot_cost)
    
