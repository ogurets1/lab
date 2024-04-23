import math

# Функция для вычисления значения выражения
def calculate_expression(x, y, z):
    result = (math.sqrt(x**2 + z**2) + math.cos(x * z)**3 + math.sqrt(y**2 + x**2) + math.cos(y * x)**3) / (math.sqrt(z**2 + y**2) + math.cos(z * y)**3)
    return result

# Ввод значений x, y и z
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

# Вычисление значения выражения
expression_value = calculate_expression(x, y, z)

# Вывод результата
print("Значение выражения:", expression_value)