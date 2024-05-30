def shuffle_cards(N, K, A):
    # 초기 카드 배치
    cards = list(range(1, N + 1))

    # K번 섞기
    for _ in range(K):
        new_cards = [0] * N  # 새로운 카드 배치 초기화
        for i, card in enumerate(cards):
            new_cards[A[i] - 1] = card  # A[i]번째 위치에 card 놓기
        cards = new_cards  # 카드 배치 업데이트

    return cards

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 카드 섞기
result = shuffle_cards(N, K, A)

# 결과 출력
print(*result)  # 언패킹하여 공백으로 구분하여 출력
