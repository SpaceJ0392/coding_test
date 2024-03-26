'''
5
4 39
43 51
49 18
89 39
116 75
178 7
'''

# n_store = int(input())
# store = [list(map(int, input().split())) for _ in range(n_store)]
# # 위치, 충전
# arrive, health = map(int, input().split())

# cnt = 0
# previous_store, now = 0, 0

# while now < n_store:   
#     now_store, now_energy = store[now] # 지금 위치
#     health -= now_store - previous_store # 잔존 체력
#     next_store, next_energy = store[now + 1] # 잠재적인 다음 위치
    
#     while next_store - now_store <= health and now < n_store:
#         now += 1
#         next_store, next_energy = store[now + 1] # 잠재적인 다음 위치
    
#     health += now_energy
#     previous_store = now_store
#     now += 1
    
# print(cnt)

n_store = int(input())
store = [list(map(int, input().split())) for _ in range(n_store + 1)]
store.reverse()
arrive, health = store[0][0], store[0][1]

def check_next(health, now):
    next, energy = store[-1]

    if health >= (next - now):
        return True
    return False

previous, cnt = 0, 0
while store:
    now, energy = store.pop()
    health -= now - previous

    # 왔는데 체력 오링이면 end
    if health < 0:
        cnt = -1
        break

    # 잔존 체력으로 갈 수 있는지 체크
    if not check_next(health, now):
        health += energy # 못가면, 충전
        cnt += 1

    # 마지막 처리
    if len(store) == 1 and health >= 0:
        break
    elif len(store) == 1 and health < 0:
        cnt = -1
        break

    # 잔존 체력 혹은 충전 후 체력으로 어디까지 갈 수 있는지
    while check_next(health, now):
        next, next_energy = store.pop()
    
    store.append([next, next_energy])
    previous = now

print(cnt)