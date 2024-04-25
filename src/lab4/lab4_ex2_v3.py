import math

# Ввод данных
a = 2.8
b = -0.3
c = 4

x = float(input("Введите значение x: "))

# Вычисление значения функции
if x < 1.2:
    y = a * x ** 2 + b * x + c
elif x == 1.2:
    y = a / x + math.sqrt(x ** 2 + 1)
else:
    y = (a + b * x) / math.sqrt(x ** 2 + 1)

# Вывод результата
print("Значение функции y =", y)
