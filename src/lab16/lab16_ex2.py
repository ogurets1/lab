# Функция для вычисления факториала числа
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Функция для вычисления значения выражения
def calculate_expression(n, m):
    result = factorial(n) / (factorial(m) * factorial(n - m))
    return result

# Ввод значений n и m
n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

# Вычисление значения выражения
expression_value = calculate_expression(n, m)

# Вывод результата
print("Значение выражения:", expression_value)