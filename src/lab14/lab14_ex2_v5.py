# Ввод данных
n = int(input("Введите количество стран: "))
countries = {}
for i in range(n):
    country_info = input().split()
    country = country_info[0]
    cities = country_info[1:]
    countries[country] = cities

# Запрос
city = input("Введите название города: ")

# Вывод
for country, cities in countries.items():
    if city in cities:
        print(country)
        break
else:
    print()