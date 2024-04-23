# Ввод количества студентов
n = int(input("количесиво студентов"))

# Создание словаря для хранения информации о студентах
students = {}
for _ in range(n):
    last_name, specialty, group = input().split()
    if specialty not in students:
        students[specialty] = []
    students[specialty].append(last_name)

# Ввод запроса
query = input()

# Поиск студентов по запросу и вывод результата
if query in students:
    print(','.join(students[query]))
else:
    print("Проверьте запрос")