def solution(prices):
    answer = []

    while prices:
        prices.reverse()
        now_prices = prices.pop()
        prices.reverse()
        turn = 0
        for price in prices:
            if now_prices > price:
                turn += 1
                break
            turn += 1

        answer.append(turn)

    return answer


print(solution([1, 2, 3, 2, 3]))
