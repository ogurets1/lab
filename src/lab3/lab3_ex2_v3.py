# Ввод двух чисел
x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

# Определение меньшего и большего чисел
min_number = min(x, y)
max_number = max(x, y)

# Замена значений
x = (min_number + max_number) / 2
y = 2 * min_number * max_number

# Вывод результата
print("Результат:", x, y)