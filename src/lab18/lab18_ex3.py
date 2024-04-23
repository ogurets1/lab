import module2

# Ввод количества чисел
N = int(input("Введите количество чисел: "))

# Ввод чисел
numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(N)]

# Вызов функции и вывод результата
result_number = module2.max_sum_of_digits(numbers)
print("Число с максимальной суммой цифр:", result_number)