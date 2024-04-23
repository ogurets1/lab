# Функция для проверки, является ли число трехзначным и делится ли оно на 8
def is_divisible_by_8_and_three_digit(number):
    return number % 8 == 0 and 100 <= number <= 999

# Подсчет суммы кубов трехзначных чисел, делящихся на 8
sum_of_cubes = sum(num**3 for num in range(100, 1000) if is_divisible_by_8_and_three_digit(num))

# Вывод результата
print("Сумма кубов всех трехзначных чисел, делящихся на 8:", sum_of_cubes)