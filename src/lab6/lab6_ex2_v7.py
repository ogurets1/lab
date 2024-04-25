# Начальное и конечное значения диапазона
start = 7
end = 37

# Инициализация суммы
sum_of_cubes = 0

# Вычисление суммы кубов нечетных чисел от start до end
for number in range(start, end + 1):
    if number % 2 != 0:
        sum_of_cubes += number ** 3

# Вывод результата
print("Сумма кубов нечетных чисел от", start, "до", end, ":", sum_of_cubes)
