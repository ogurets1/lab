import random

# Ввод количества экзаменов
num_exams = int(input("Введите количество экзаменов: "))

# Ввод названий дисциплин
subjects = input("Введите названия дисциплин через запятую и пробел: ").split(", ")

# Генерация списка дней недели и времени экзаменов
days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
exam_times = [9.0 + 0.5 * i for i in range(10)]

# Вывод информации о каждом экзамене
for i in range(num_exams):
    day_of_week = random.choice(days_of_week)
    exam_time = random.choice(exam_times)
    lucky_ticket = random.randint(1, 20)
    print(f"Экзамен по дисциплине «{subjects[i]}» состоится в {day_of_week} время {exam_time:.1f}. Ваш счастливый билет № {lucky_ticket}.")
