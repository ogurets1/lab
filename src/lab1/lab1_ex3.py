# Ввод трех целых чисел с клавиатуры
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

# Находим сумму
summa = a + b + c
# Находим произведение
product = a * b * c
# Находим среднее арифметическое
average = summa / 3

print("Сумма:", summa)
print("Произведение:", product)
print("Среднее арифметическое:", average)