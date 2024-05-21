n = int(input())


def get_triangle(tot):
    temp = dict()
    for a in range(3, tot, 1):
        a, b, c = a, (a**2 - 1) // 2, (a**2 + 1) // 2
        if temp.get(a + b + c) == None:
            temp.setdefault(a + b + c, 1)
        else:
            temp[a + b + c] += 1

    return temp


max_round, max_cnt = 0, 0
triangle_list = get_triangle(n)

print(triangle_list)
print(max_round, max_cnt)
