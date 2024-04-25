# Ввод трех действительных чисел
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# Возведение чисел в квадрат, если они неотрицательные, и в четвертую степень - если отрицательные
a_squared, b_squared, c_squared = [a ** (2 if x >= 0 else 4) for x in (a, b, c)]


# Вывод результатов
print("Результат возведения в квадрат или в четвертую степень:")
print("Для числа a:", a_squared)
print("Для числа b:", b_squared)
print("Для числа c:", c_squared)