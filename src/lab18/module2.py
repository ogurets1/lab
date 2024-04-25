def sum_of_digits(number):
    """
    Функция для нахождения суммы цифр числа.
    
    Args:
        number (int): Целое число.
        
    Returns:
        int: Сумма цифр числа.
    """
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    return sum_digits


def number_with_max_sum(numbers):
    """
    Функция для выбора числа с максимальной суммой цифр из списка.

    Args:
        numbers (list): Список целых чисел.

    Returns:
        int: Число с максимальной суммой цифр.
    """
    max_sum = float('-inf')
    number_with_max = None
    for number in numbers:
        current_sum = sum_of_digits(number)
        if current_sum > max_sum:
            max_sum = current_sum
            number_with_max = number
    return number_with_max