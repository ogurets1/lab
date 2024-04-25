# Ввод чисел и интервала
numbers = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите начальный и конечный номера интервала (через пробел): ").split())

# Вычисление суммы чисел в интервале
sum_of_interval = sum(numbers[start:end+1])

# Вывод результата
print("Сумма чисел в интервале:", sum_of_interval)