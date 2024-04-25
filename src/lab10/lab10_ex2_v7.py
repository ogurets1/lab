# Ввод строки
sequence = input("Введите последовательность символов: ")

# Создание множества
char_set = set()

# Добавление знаков препинания и букв от 'E' до 'N' в множество
for char in sequence:
    if char in [',', '.', ';', ':']:
        char_set.add(char)
    elif char.isalpha():
        if char >= 'E' and char <= 'N':
            char_set.add(char)

# Вывод множества знаков препинания и букв от 'E' до 'N'
print("Множество знаков препинания и букв от 'E' до 'N':", char_set)