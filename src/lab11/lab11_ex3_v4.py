# Ввод списка из 12 вещественных чисел
numbers = [float(input(f"Введите число {i+1}: ")) for i in range(12)]

# Находим индекс наименьшего элемента
min_index = numbers.index(min(numbers))

# Меняем местами первый элемент и элемент с наименьшим значением
numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

# Вывод результата
print("Список после замены наименьшего элемента с первым:", numbers)