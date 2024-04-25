# Ввод последовательности
sequence = [int(input(f"Введите число {i+1}: ")) for i in range(18)]

# Фильтрация четных чисел
even_numbers = [num for num in sequence if num % 2 == 0]

# Вывод результата
if even_numbers:
    print("Список четных чисел:", even_numbers)
else:
    print("В последовательности нет четных чисел.")