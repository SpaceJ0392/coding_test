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

cnt = 0
previous_store, now = 0, 0

while now < n_store:   
    now_store, now_energy = store[now] # 지금 위치
    health -= now_store - previous_store # 잔존 체력
    next_store, next_energy = store[now + 1] # 잠재적인 다음 위치
    
    while next_store - now_store <= health and now < n_store:
        now += 1
        next_store, next_energy = store[now + 1] # 잠재적인 다음 위치
    
    health += now_energy
    previous_store = now_store
    now += 1
    
print(cnt)

    
    