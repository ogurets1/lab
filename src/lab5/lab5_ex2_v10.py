# Ввод данных
A = float(input("Введите размер стипендии студента (руб.): "))
B = float(input("Введите ежемесячные расходы на проживание (руб.): "))
increase_rate = 0.03  # Увеличение расходов каждый месяц

# Вычисление общих расходов на учебный год
total_expenses = 0
for month in range(10):
    total_expenses += B
    B *= (1 + increase_rate)  # Увеличение расходов на следующий месяц

# Вычисление необходимой суммы денег
required_money = total_expenses - 10 * A

# Вывод результата
print("Необходимая сумма денег:", required_money, "руб.")