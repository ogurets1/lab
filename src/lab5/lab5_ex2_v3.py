# Задаем начальное количество амеб
amoeba = 1

# Инициализируем переменную для подсчета прошедших часов
hours = 0

# Пока прошло менее 24 часов, продолжаем удваивать количество амеб каждые 3 часа
while hours < 24:
    # Каждые 3 часа количество амеб удваивается
    if hours % 3 == 0 and hours != 0:
        amoeba *= 2
    # Увеличиваем счетчик прошедших часов
    hours += 1

# Выводим результат
print("Через 24 часа будет", amoeba, "амеб")
