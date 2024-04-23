import datetime

# Ввод количества дней до экзамена
K = int(input("Введите количество дней до экзамена: "))

# Вычисление даты экзамена
exam_date = datetime.datetime.now() + datetime.timedelta(days=K)

# Вывод даты экзамена
print("Дата экзамена:", exam_date.strftime("%d.%m"))