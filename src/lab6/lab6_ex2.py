# Задаем значение переменной n
n = 15

# Инициализируем переменные для хранения суммы и произведения чисел
sum_numbers = 0
product_numbers = 1

# Ввод чисел и вычисление суммы и произведения
for i in range(n):
    number = float(input(f"Введите число {i + 1}: "))
    sum_numbers += number
    product_numbers *= number

# Вывод результата
print("Сумма введенных чисел:", sum_numbers)
print("Произведение введенных чисел:", product_numbers)