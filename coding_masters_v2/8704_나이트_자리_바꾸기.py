chess_map = [list(input()) for _ in range(3)]
print('possible') if chess_map[1][1] == '0' else print('impossible')