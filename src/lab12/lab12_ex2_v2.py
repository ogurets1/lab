# Ввод матрицы
n = int(input("Введите размерность квадратной матрицы: "))
matrix = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

# Вычисление суммы элементов каждой строки
row_sums = [sum(matrix[i]) for i in range(n)]

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(row)
print("Суммы элементов каждой строки:", row_sums)