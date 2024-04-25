# Функция для проверки числа на трехзначность и деление на 6
def is_three_digit_and_divisible_by_6(num):
    return num >= 100 and num <= 999 and num % 6 == 0

# Функция для извлечения трехзначных четных чисел, делимых на 6, из списка
def extract_numbers_divisible_by_6(lst):
    return [num for num in lst if is_three_digit_and_divisible_by_6(num)]

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для извлечения чисел, делимых на 6
result = extract_numbers_divisible_by_6(numbers)

# Вывод результата
print("Трехзначные четные числа, делимые на 6:", result)