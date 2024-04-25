import module1

# Ввод списка чисел и значения K с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
k = int(input("Введите значение K: "))

# Вызов функции для подсчета элементов, превышающих K
count = module1.count_elements_above_k(numbers, k)

# Вывод результата
print("Количество элементов списка, превышающих K:", count)
