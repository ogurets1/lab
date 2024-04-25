# Функция для проверки числа на положительность
def is_positive(num):
    return num > 0

# Функция для вычисления квадрата числа
def square(num):
    return num ** 2

# Функция для вычисления суммы квадратов положительных чисел списка
def sum_of_positive_squares(lst):
    return sum(square(num) for num in lst if is_positive(num))

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции и вывод результата
print("Сумма квадратов положительных чисел списка:", sum_of_positive_squares(numbers))