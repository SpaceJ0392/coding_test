def min_trades_to_make_windows(N, a, b):
    trades = 0
    frames = 1  # 초기 창틀 수

    # Step 1: 확보해야 하는 창틀의 수를 최대한 빠르게 늘리기
    while frames < N:
        if a > 1:
            additional_frames = frames * (a - 1)
            frames += additional_frames
            trades += 1
        else:
            break

    # Step 2: 충분히 창틀을 확보한 후, 유리를 얻기 위해 거래
    while frames < N + N:
        if frames >= b:
            frames -= b - 1
            trades += 1
        else:
            break

    # Step 3: 남은 부족한 창틀과 유리를 위해 추가 거래
    trades += N - 1

    return trades

# 입력 받기
N, a, b = map(int, input().strip().split())

# 결과 출력
result = min_trades_to_make_windows(N, a, b)
print(result)
