# Функция для фильтрации списка чисел
def filter_numbers(numbers):
    # Фильтрация списка
    filtered_numbers = [num for num in numbers if num > 10 and num % 2 == 0]
    return filtered_numbers

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Фильтрация списка и вывод результата
filtered_numbers = filter_numbers(numbers)
if filtered_numbers:
    print("Отфильтрованный список:", filtered_numbers)
else:
    print("В списке нет четных чисел больше 10.")

