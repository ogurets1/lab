# Ввод данных
n = int(input("Введите значение переменной n: "))

# Инициализация переменных
i = 1
summa = 0

# Цикл с условием
while i <= n:
    # Вывод текущих значений переменных
    print("Текущее значение i:", i)
    print("Текущее значение summa:", summa)
    # Увеличение суммы на i и инкремент переменной i
    summa += i
    i += 1

# Вывод результата
print("Итоговое значение summa:", summa)