# Ввод данных
start_amoeba_count = int(input("Введите начальное количество амеб: "))
division_interval = int(input("Введите интервал деления амеб (в часах): "))
hours = int(input("Введите количество часов для рассмотрения: "))

# Вычисление количества амеб через каждые division_interval часов
amoeba_count = start_amoeba_count
for hour in range(division_interval, hours + 1, division_interval):
    amoeba_count *= 2  # Удваиваем количество амеб
    print("Через", hour, "часа(ов) будет", amoeba_count, "амеб(ы)")
