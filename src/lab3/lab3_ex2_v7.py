# Ввод трех чисел
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

# Подсчет количества двузначных чисел
count = 0
if 10 <= abs(a) < 100:
    count += 1
if 10 <= abs(b) < 100:
    count += 1
if 10 <= abs(c) < 100:
    count += 1

# Вывод результата
print("Количество двузначных чисел среди a, b и c:", count)
