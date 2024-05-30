def is_point_in_polygon(polygon, point):
    x, y = point
    n = len(polygon)
    inside = False

    px1, py1 = polygon[0]
    for i in range(n + 1):
        px2, py2 = polygon[i % n]
        if y > min(py1, py2):
            if y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xinters:
                        inside = not inside
        px1, py1 = px2, py2

    return inside

def all_points_in_polygon(polygon, points):
    for point in points:
        if not is_point_in_polygon(polygon, point):
            return False
    return True

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

polygon = []
index = 2
for _ in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    polygon.append((x, y))
    index += 2

points = []
for _ in range(M):
    x = int(data[index])
    y = int(data[index + 1])
    points.append((x, y))
    index += 2

# Check if all points are inside the polygon
if all_points_in_polygon(polygon, points):
    print("YES")
else:
    print("NO")
