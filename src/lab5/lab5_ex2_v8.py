# Инициализируем переменную для хранения суммы кубов
sum_of_cubes = 0

# Вычисляем сумму кубов нечетных чисел от 7 до 37
for i in range(7, 38, 2):
    sum_of_cubes += i ** 3

# Вывод результата
print("Сумма кубов нечетных чисел от 7 до 37:", sum_of_cubes)
