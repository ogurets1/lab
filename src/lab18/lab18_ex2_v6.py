import module1

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для вычисления произведения элементов
result = module1.product_of_elements(numbers)

# Вывод результата
print("Произведение значений элементов списка:", result)