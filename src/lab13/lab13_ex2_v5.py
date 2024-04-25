# Ввод чисел и интервала
numbers = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите начальный и конечный номера интервала (через пробел): ").split())

# Вычисление суммы квадратов чисел в интервале
sum_of_squares = sum(number ** 2 for number in numbers[start:end+1])

# Вывод результата
print("Сумма квадратов чисел в интервале:", sum_of_squares)