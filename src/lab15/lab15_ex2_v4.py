def print_sum_and_product(numbers):
    if not numbers:
        print("0")
    else:
        total_sum = sum(numbers)
        total_product = 1
        for num in numbers:
            total_product *= num
        print("Сумма элементов:", total_sum)
        print("Произведение элементов:", total_product)

# Ввод списка с клавиатуры
numbers = list(map(float, input("Введите список вещественных чисел, разделенных пробелами: ").split()))

# Вызов функции
print_sum_and_product(numbers)