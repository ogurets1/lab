import math

# Ввод данных
t = 2.2
x = float(input("Введите значение x: "))

# Вычисление значения функции
if x < 0.5:
    y = (math.log(x + x ** 2)) / math.sqrt(x + t)
elif x == 0.5:
    y = math.sqrt(x + t) + 1 / x
else:
    y = math.cos(x) + math.sin(x) ** 2

# Вывод результата
print("Значение функции y =", y)
