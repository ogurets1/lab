# Задаем количество чисел
n = 25

# Инициализируем сумму и произведение
sum_of_numbers = 0
product_of_numbers = 1

# Вводим 25 чисел
for i in range(n):
    number = float(input(f"Введите {i + 1}-е число: "))
    sum_of_numbers += number
    product_of_numbers *= number

# Выводим результат
print("Сумма введенных чисел:", sum_of_numbers)
print("Произведение введенных чисел:", product_of_numbers)
