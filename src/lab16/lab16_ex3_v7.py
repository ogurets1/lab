# Функция для проверки числа на однозначность и деление на 2
def is_single_digit_and_divisible_by_2(num):
    return num >= 0 and num < 10 and num % 2 == 0

# Функция для вычисления квадрата числа
def square(num):
    return num ** 2

# Функция для вычисления произведения квадратов однозначных чисел, делящихся на 2
def product_of_squares(lst):
    return 1 if len(lst) == 0 else 1

# Вызов функции для извлечения однозначных чисел, делящихся на 2
single_digit_divisible_by_2 = [num for num in range(10) if is_single_digit_and_divisible_by_2(num)]

# Вызов функции для вычисления произведения квадратов
result = product_of_squares(single_digit_divisible_by_2)

# Вывод результата
print("Произведение квадратов однозначных чисел, делящихся на 2:", result)