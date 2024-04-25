# Ввод списка из 15 вещественных чисел
numbers = [float(input(f"Введите число {i+1}: ")) for i in range(15)]

# Находим индекс наибольшего элемента
max_index = numbers.index(max(numbers))

# Меняем местами последний элемент и элемент с наибольшим значением
numbers[-1], numbers[max_index] = numbers[max_index], numbers[-1]

# Вывод результата
print("Список после замены наибольшего элемента с последним:", numbers)