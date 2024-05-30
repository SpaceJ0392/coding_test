N_final, M_final = 0, 0
def play_money_game(N, M):
    global N_final, M_final
    
    # 게임이 종료될 때까지 반복
    if N == 0 or M == 0: 
        N_final, M_final = N, M
        return 
    
    elif N < 0 or M < 0: 
        return
    
    # 민서의 돈이 윤호의 돈의 2배 이상인 경우
    elif N >= 2 * M:  
        play_money_game(N - 2 * M, M)
        
    # 윤호의 돈이 민서의 돈의 2배 이상인 경우
    elif M >= 2 * N: 
        play_money_game(N, M - 2 * N)
        
    # 게임이 종료될 경우
    elif M < 2 * N and N < 2 * M: 
        N_final, M_final = N, M
        return  

N, M = map(int, input().split())
play_money_game(N, M)
print(N_final, M_final)

