# Функция для проверки числа на нечетность и деление на 11
def is_odd_and_divisible_by_11(num):
    return num % 2 != 0 and num % 11 == 0

# Функция для извлечения нечетных чисел, делимых на 11, из списка
def extract_numbers_divisible_by_11(lst):
    return [num for num in lst if is_odd_and_divisible_by_11(num)]

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для извлечения чисел, делимых на 11
result = extract_numbers_divisible_by_11(numbers)

# Вывод результата
print("Нечетные числа, делимые на 11:", result)