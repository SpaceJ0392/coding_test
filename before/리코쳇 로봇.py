from collections import deque


def solution(board):
    goal_y, goal_x = -1, -1
    start_y, start_x = -1, -1

    board = [list(board[i]) for i in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "R":
                start_y, start_x = y, x
            if board[y][x] == "G":
                goal_y, goal_x = y, x

            board[y][x] = float("inf")

    dir_y = [-1, 0, 0, 1]
    dir_x = [0, 1, -1, 0]
    path = deque([[start_y, start_x, 0]])
    while path:
        if board[goal_y][goal_x] != float("inf"):
            return board[goal_y][goal_x]

        now_y, now_x, cnt = path.popleft()

        for i in range(len(dir_y)):
            cnt += 1

            while 0 <= now_y + dir_y[i] < len(board) and 0 <= now_x + dir_x[i] < len(board[0]) and board[now_y + dir_y[i]][now_x + dir_x[i]] != "D":
                now_y, now_x = now_y + dir_y[i], now_y + dir_x[i]

            if cnt < board[now_y][now_x]:
                board[now_y][now_x] = cnt
                path.append([now_y, now_x, cnt])

    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
