n, a, b = map(int, input().split())

frame_need = n + (n * b)
frame_trade_cnt = 0
if a - 1 != 1:
    if frame_need % (a - 1) == 0:
        frame_trade_cnt = (frame_need // (a - 1))
    else:
        frame_trade_cnt = (frame_need // (a - 1)) + 1
else:
    frame_trade_cnt = frame_need - 1

print(frame_trade_cnt + n)