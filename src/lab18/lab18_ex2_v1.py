import module1

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
k = int(input("Введите значение K: "))

# Вызов функции для переписывания элементов
result = module1.copy_without_k(numbers, k)

# Вывод результата
print("Список без элементов, равных K:", result)
