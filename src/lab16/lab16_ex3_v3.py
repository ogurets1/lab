# Функция для проверки числа на четность
def is_even(num):
    return num % 2 == 0

# Функция для печати четных чисел из списка
def print_even_numbers(lst):
    even_numbers = [num for num in lst if is_even(num)]
    print("Четные числа из списка:", even_numbers)

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для печати четных чисел
print_even_numbers(numbers)