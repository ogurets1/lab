# Задаем значение k
k = 3

# Инициализируем сумму
sum_of_numbers = 0

# Начальное значение числа
number = 1000

# Пока число не превышает 9999
while number <= 9999:
    # Если число кратно k, добавляем его к сумме
    if number % k == 0:
        sum_of_numbers += number
    number += 1

# Вывод результата
print("Сумма всех 4-значных чисел, кратных", k, ":", sum_of_numbers)
