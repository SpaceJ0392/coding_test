def pascal_tetrahedron(n):
    tetrahedron = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(tetrahedron[i-1][j-1] + tetrahedron[i-1][j])
        tetrahedron.append(row)
    return tetrahedron

def print_pascal_tetrahedron(tetrahedron):
    for row in tetrahedron:
        print(" ".join(map(str, row)).center(len(tetrahedron[-1]) * 3))

n = 3
tetrahedron = pascal_tetrahedron(n)
print_pascal_tetrahedron(tetrahedron)