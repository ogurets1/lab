# Ввод данных
n = int(input("Введите количество одноклассников: "))
birthdays = {}
for i in range(n):
    birthday_info = input().split()
    name = birthday_info[0]
    day, month = birthday_info[1:]
    birthdays[name] = day

# Запрос
month = input("Введите название месяца: ")

# Вывод
if month in birthdays.values():
    result = [(name, birthdays[name]) for name in birthdays if birthdays[name].startswith(month)]
    print(*[f"{name} {day}" for name, day in result], sep=' ')
else:
    print()