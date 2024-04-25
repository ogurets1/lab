import module2
# Ввод списка чисел
numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

# Нахождение числа с максимальной суммой цифр
result = module2.number_with_max_sum(numbers)

# Вывод результата
print(f"Число с максимальной суммой цифр: {result}")