# Ввод матрицы
n = int(input("Введите размерность квадратной матрицы: "))
matrix = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

# Поиск минимального элемента матрицы
min_value = matrix[0][0]
min_row, min_column = 0, 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_row, min_column = i, j

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(row)
print(f"Минимальный элемент матрицы: {min_value}, его индексы: ({min_row+1}, {min_column+1})")