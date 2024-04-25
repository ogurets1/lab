import module1

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для поиска максимального элемента
max_value = module1.find_max(numbers)

# Вывод результата
print("Максимальный элемент списка:", max_value)