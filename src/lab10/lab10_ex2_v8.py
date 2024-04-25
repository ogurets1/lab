# Ввод строки
sequence = input("Введите последовательность символов: ")

# Создание множества
char_set = set()

# Добавление знаков арифметических операций и операций отношения в множество
for char in sequence:
    if char in ['+', '-', '*', '/', '<', '>', '=', '!']:
        char_set.add(char)

# Вывод множества знаков арифметических операций и операций отношения
print("Множество знаков арифметических операций и операций отношения:", char_set)