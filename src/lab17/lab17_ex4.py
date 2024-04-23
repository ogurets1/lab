import datetime

def is_happy_day(date):
    # Проверка, что день не кратен 4 и не понедельник
    return date.day % 4 != 0 and date.weekday() != 0

# Ввод исходной даты
input_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
year, month, day = map(int, input_date.split('/'))
start_date = datetime.datetime(year, month, day)

# Ввод значения n
n = int(input("Введите число n: "))

# Поиск трех счастливых дат
happy_dates = []
while len(happy_dates) < 3:
    if is_happy_day(start_date):
        happy_dates.append(start_date)
    start_date += datetime.timedelta(days=n)

# Вывод счастливых дат
print("Счастливые даты экзамена:")
for date in happy_dates:
    print(date.strftime("%d %B, %A"))
