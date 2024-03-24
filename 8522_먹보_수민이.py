n_store = int(input())
store = [list(map(int, input().split())) for _ in range(n_store)]
# 위치, 충전
arrive, health = map(int, input().split())
store.append([arrive, 0])
store.reverse()

now, cnt = 0, 0
previous_store = 0
while arrive > now:
    now_store, energy = store.pop() # 지금 편의점
    next_store, next_energy = store[-1] # 다음 편의점
    
    health -= now_store - previous_store # 잔존 체력
    delta_store = next_store - now_store # 다음 편의점까지의 거리
    if delta_store > health: 
        health += energy
        cnt += 1
    else: store.pop() # 체력에 여유 있으면, 편의점 1개 pass
    
    previous_store = now_store

print(cnt)
    
    