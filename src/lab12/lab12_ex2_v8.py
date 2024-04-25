# Ввод матрицы
n = int(input("Введите размерность квадратной матрицы: "))
matrix = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

# Сортировка элементов каждой строки по возрастанию
sorted_matrix = [sorted(row) for row in matrix]

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(row)
print("Матрица с элементами каждой строки, упорядоченными по возрастанию:")
for row in sorted_matrix:
    print(row)