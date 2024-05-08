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

    if health > (next - now):
        return True
    
    return False

previous, cnt = 0, 0
while len(store) > 1:
    now, energy = store.pop()
    health -= now - previous

    if health < 0:
        cnt = -1
        break

    # 잔존 체력으로 갈 수 있는지 체크
    if not check_next(health, now):
        health += energy # 못가면, 충전
        cnt += 1

    #충전 후 체력으로 갈 수 있는지 체크
    if not check_next(health, now):
        cnt = -1 # 못가면, 종료
        break

    previous = now

if len(store) == 1 and health < arrive - previous:
    print(-1)
else:
    print(cnt)