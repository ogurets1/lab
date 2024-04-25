# Функция для проверки числа на деление на 17
def divisible_by_17(num):
    return num % 17 == 0

# Функция для извлечения чисел, делимых на 17, из списка
def extract_numbers_divisible_by_17(lst):
    return [num for num in lst if divisible_by_17(num)]

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для извлечения чисел, делимых на 17
result = extract_numbers_divisible_by_17(numbers)

# Вывод результата
print("Числа, делимые на 17:", result)