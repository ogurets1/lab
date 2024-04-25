# Ввод матрицы
n = int(input("Введите размерность квадратной матрицы: "))
matrix = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

# Вычисление суммы отрицательных элементов под дополнительной диагональю
additional_diagonal_sum = sum(matrix[i][j] for i in range(n) for j in range(n) if i + j > n - 1 and matrix[i][j] < 0)

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(row)
print("Сумма отрицательных элементов под дополнительной диагональю:", additional_diagonal_sum)