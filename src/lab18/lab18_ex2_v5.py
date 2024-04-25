import module1

# Ввод списка чисел и значения K с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
k = int(input("Введите значение K: "))

# Вызов функции для вычисления суммы элементов, меньших K
result = module1.sum_of_elements_below_k(numbers, k)

# Вывод результата
print("Сумма значений элементов списка, меньших K:", result)
