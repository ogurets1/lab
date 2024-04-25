import module1

# Ввод упорядоченного списка чисел и значения K с клавиатуры
numbers = list(map(int, input("Введите упорядоченный список чисел через пробел: ").split()))
k = int(input("Введите значение K для вставки: "))

# Вызов функции для вставки значения K
module1.insert_into_sorted_list(numbers, k)

# Вывод результата
print("Список после вставки значения K:", numbers)
