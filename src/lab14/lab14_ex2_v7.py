# Ввод данных
n = int(input("Введите количество одноклассников: "))
birthdays = {}
for i in range(n):
    birthday_info = input().split()
    name = birthday_info[0]
    day, month = birthday_info[1:]
    birthdays[name] = (day, month)

# Запрос
month = input("Введите название месяца: ")

# Вывод
if month in [birthday[1] for birthday in birthdays.values()]:
    print(*[name for name, birthday in birthdays.items() if birthday[1] == month], sep=' ')
else:
    print()