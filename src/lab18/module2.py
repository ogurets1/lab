def sum_of_digits(number):
    """
    Функция находит сумму цифр числа.
    """
    return sum(int(digit) for digit in str(number))


def max_sum_of_digits(numbers):
    """
    Функция выбирает число с максимальной суммой цифр.
    """
    max_number = numbers[0]
    max_sum = sum_of_digits(max_number)

    for number in numbers[1:]:
        current_sum = sum_of_digits(number)
        if current_sum > max_sum:
            max_number = number
            max_sum = current_sum

    return max_number