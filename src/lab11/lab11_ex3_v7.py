# Ввод списка из 10 целых чисел
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(10)]

# Разделение списка на положительные и отрицательные числа
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num <= 0]

# Объединение списков с сохранением порядка
numbers = positive_numbers + negative_numbers

# Вывод результата
print("Список после разделения на положительные и отрицательные числа:", numbers)