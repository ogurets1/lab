# Функция для фильтрации списка чисел и подсчета суммы оставшихся элементов
def process_lists(numbers, a, b, c):
    filtered_numbers = [num for num in numbers if a < num < b and num % c == 0]
    other_numbers_sum = sum(num for num in numbers if num not in filtered_numbers)
    return filtered_numbers, other_numbers_sum

# Ввод списков с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
a, b, c = map(int, input("Введите три числа a, b, c через пробел: ").split())

# Вызов функции и вывод результата
filtered_numbers, other_numbers_sum = process_lists(numbers, a, b, c)
print("Элементы, которые одновременно больше {}, меньше {} и делятся на {} без остатка:".format(a, b, c), filtered_numbers)
print("Сумма остальных элементов списка:", other_numbers_sum)
