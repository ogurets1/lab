import math

# Ввод параметров функции
a = float(input("Введите значение параметра 'a': "))
b = float(input("Введите значение параметра 'b': "))
x = float(input("Введите значение переменной 'x': "))

# Вычисление значения функции
result = math.sin((x**2+a)**2)**3-math.sqrt(x/b)

# Вывод результата
print("Значение y =",result)