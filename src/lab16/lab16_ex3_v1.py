# Функция для проверки числа на трехзначность и деление на 8
def is_three_digit_and_divisible_by_8(num):
    return num >= 100 and num <= 999 and num % 8 == 0

# Функция вычисления куба числа
def cube(num):
    return num ** 3

# Функция вычисления суммы кубов всех трехзначных чисел, делящихся на 8
def sum_of_cubes(lst):
    return sum(cube(num) for num in lst if is_three_digit_and_divisible_by_8(num))

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции и вывод результата
print("Сумма кубов всех трехзначных чисел, делящихся на 8:", sum_of_cubes(numbers))