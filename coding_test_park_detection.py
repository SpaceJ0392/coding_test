def solution(park, routes):
    answer = []

    # 시작 지점
    y = 0
    for line in park:
        if "S" in line:
            answer = [y, line.index("S")]
            break
        y += 1

    routes_dict = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}
    y, x = answer  # start 위치
    y_size, x_size = len(park), len(park[0])  # 맵의 크기

    for route in routes:
        route = route.split(" ")
        route[1] = int(route[1])

        y_before, x_before = y, x
        for time in range(route[1]):
            dy, dx = routes_dict.get(route[0])  # 이동할 위치
            yy, xx = y + dy, x + dx

            if yy >= y_size or yy < 0 or xx >= x_size or xx < 0:
                y, x = y_before, x_before
                break

            if park[yy][xx] == "X":
                y, x = y_before, x_before
                break

            y = yy
            x = xx

    answer = [y, x]
    return answer


print(solution(	["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
