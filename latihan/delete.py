mat1 = [
    [5, 4, 6, 7, 2],
    [2, 6, 4, 3, 2],
    [4, 6, 2, 5, 6],
    [9, 2, 1, 5, 2],
    [1, 3, 5, 3, 4],
]

mat2 = [
    [1, 0, 3, 6, 3],
    [4, 2, 2, 6, 1],
    [7, 7, 9, 3, 6],
    [2, 1, 5, 6, 8],
    [9, 6, 4, 8, 2],
]

mat3 = []

for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)


for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print (mat3[x][y], end=' ')
    print ()