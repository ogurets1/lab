import math

# Ввод данных
a = -0.5
b = 2
t = float(input("Введите значение x: "))

# Вычисление значения функции
if 1 <= t <= 2:
    y = a * t ** 2 * math.log(t)
elif t < 1:
    y = 1
else:
    y = math.e ** a * t * math.cos(b * t)

# Вывод результата
print("Значение функции y =", y)
