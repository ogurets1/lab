# Функция для проверки числа на отрицательность
def is_negative(num):
    return num < 0

# Функция вычисления куба числа
def cube(num):
    return num ** 3

# Функция вычисления суммы кубов отрицательных чисел списка
def sum_of_negative_cubes(lst):
    return sum(cube(num) for num in lst if is_negative(num))

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции и вывод результата
print("Сумма кубов отрицательных чисел списка:", sum_of_negative_cubes(numbers))