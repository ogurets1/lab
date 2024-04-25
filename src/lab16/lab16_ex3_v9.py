# Функция для проверки числа на двузначность и деление на 7
def is_two_digit_and_divisible_by_7(num):
    return num >= 10 and num <= 99 and num % 7 == 0

# Функция для вычисления квадрата числа
def square(num):
    return num ** 2

# Функция для вычисления суммы квадратов двузначных чисел, делящихся на 7
def sum_of_squares(lst):
    return sum(square(num) for num in lst if is_two_digit_and_divisible_by_7(num))

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции и вывод результата
print("Сумма квадратов всех двузначных чисел, делящихся на 7:", sum_of_squares(numbers))