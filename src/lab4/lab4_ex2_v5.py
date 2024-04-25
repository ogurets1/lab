import math

# Ввод данных
a = 2.5
x = float(input("Введите значение x: "))

# Вычисление значения функции
if x > a:
    y = x * ((x - a) ** (1 / 3))
elif x == a:
    y = x * math.sin(a * x)
else:
    y = math.exp(-a * t) * math.cos(a * x)

# Вывод результата
print("Значение функции y =", y)
