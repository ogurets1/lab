# Ввод данных
A = float(input("Введите размер стипендии студента (руб.): "))
B = float(input("Введите расходы на проживание в месяц (руб.): "))

# Расчет суммы денег, необходимой на 10 месяцев
total_money = A + B  # Изначально на один месяц

for i in range(2, 11):
    B *= 1.03  # Увеличиваем расходы на 3% каждый месяц
    total_money += A + B

# Вывод результата
print("Сумма денег, необходимая на 10 месяцев:", total_money, "руб.")