# Ввод списка Z
Z = [int(input(f"Введите элемент {i+1}: ")) for i in range(20)]

# Фильтрация положительных элементов и нахождение минимального значения
positive_values = [num for num in Z if num > 0]
if positive_values:
    min_positive = min(positive_values)
    print("Наименьший положительный элемент:", min_positive)
else:
    print("В списке нет положительных элементов.")