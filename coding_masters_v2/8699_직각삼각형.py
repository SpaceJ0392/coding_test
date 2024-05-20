n = int(input())

def get_triangle(perimeter):
    cnt = 0
    visited = set()
    for a in range(3, perimeter // 3 + 1):
        for b in range(4, (perimeter - a) // 2 + 1 ):
            c = perimeter - a - b
            if a * a + b * b == c * c:
                cnt += 1

    return cnt

max_round, max_cnt = 0, 0
for i in range(n, 11, -1):
    cnt = get_triangle(i)
    if cnt != 0 and max_cnt < cnt:
        max_round, max_cnt = i, cnt

print(max_round, max_cnt)