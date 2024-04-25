import module1

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функций для нахождения количества и значения максимального элемента
max_value = module1.find_max(numbers)
count = module1.count_max_elements(numbers)

# Вывод результата
print("Максимальный элемент списка:", max_value)
print("Количество максимальных элементов в списке:", count)
