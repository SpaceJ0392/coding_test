def play_money_game(N, M):
    # 게임이 종료될 때까지 반복
    if N <= 0 or M <= 0:
        if N <= 0: N = 0
        if M <= 0: M = 0
        return N, M
    # 민서의 돈이 윤호의 돈의 2배 이상인 경우
    elif N >= 2 * M: return play_money_game(N - 2 * M, M)
    # 윤호의 돈이 민서의 돈의 2배 이상인 경우
    elif M >= 2 * N: return play_money_game(N, M - 2 * N)

    else: return N, M # 게임이 종료될 경우
        
        


N, M = map(int, input().split())
N_final, M_final = play_money_game(N, M)
print(N_final, M_final)

