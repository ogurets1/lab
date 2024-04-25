# Ввод списка из 10 вещественных чисел
numbers = [float(input(f"Введите число {i+1}: ")) for i in range(10)]

# Сортировка списка по убыванию
numbers.sort(reverse=True)

# Вывод результата
print("Список после сортировки по убыванию:", numbers)