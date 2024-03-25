'''
5
4 39
43 51
49 18
89 39
116 75
178 7
'''

n_store = int(input())
store = [list(map(int, input().split())) for _ in range(n_store)]
# 위치, 충전
arrive, health = map(int, input().split())
store.append([arrive, 0])
store.reverse()

cnt = 0
now_store, previous_store = 0, 0

while arrive > now_store and len(store) > 1:
    now_store, energy = store.pop() # 지금 편의점
    next_store, next_energy = store[-1] # 다음 편의점

    real_next_store, real_next_energy = 0, 0
    if len(store) > 1:
        while delta_store <= health:
            real_next_store, real_next_energy = store.pop()
            next_store, next_energy = store[-1]

            delta_store = next_store - now_store
        
        store.append([real_next_store, real_next_energy])

    health -= now_store - previous_store # 잔존 체력
    health += energy
    cnt += 1

    delta_store = next_store - now_store # 다음 편의점까지의 거리
    if delta_store > health:
        cnt = -1
        break

    
    
    previous_store = now_store

#TODO - 마지막 처리

print(cnt)
    
    