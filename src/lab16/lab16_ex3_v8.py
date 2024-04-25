# Функция для проверки числа на нечетность
def is_odd(num):
    return num % 2 != 0

# Функция для печати нечетных чисел из списка
def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if is_odd(num)]
    print("Нечетные числа из списка:", odd_numbers)

# Ввод списка чисел с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Вызов функции для печати нечетных чисел
print_odd_numbers(numbers)