# Fungsi untuk mengalikan dua matriks
def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Matriks pertama (5x5)
matrix1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Matriks kedua (5x5)
matrix2 = [
    [2, 3, 6, 2, 2],
    [3, 4, 5, 6, 1],
    [3, 3, 5, 12, 13],
    [1, 4, 4, 7, 9],
    [4, 4, 5, 7, 9]
]

# Panggil fungsi perkalian matriks
result_matrix = multiply_matrices(matrix1, matrix2)

# Tampilkan hasil
print("Hasil Perkalian Matriks:")
for row in result_matrix:
    print(row)

    # Nama : Muhammad Rangga Maulana 
    # NIM : 17230606
   
    # Nama : Muhammad Alfarizki 
    # NIM :17231004
    
    # Kelas : 17.1B.01
