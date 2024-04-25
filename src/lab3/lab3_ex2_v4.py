# Ввод двух чисел
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

# Проверка условий и замена значений
if m != n:
    replacement = max(m, n)
    m = replacement
    n = replacement
else:
    m = 0
    n = 0

# Вывод результата
print("Результат:", m, n)