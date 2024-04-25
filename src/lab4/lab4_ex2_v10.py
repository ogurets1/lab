import math

# Ввод данных
b = 1.5
x = float(input("Введите значение x: "))

# Вычисление значения функции
if x < 1:
    y = b * x - math.log(b * x)
elif x == 1:
    y = 1
else:
    y = 1 / (b * x + math.log(b * x))

# Вывод результата
print("Значение функции y =", y)
