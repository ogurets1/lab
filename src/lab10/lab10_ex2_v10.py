# Ввод строки
sequence = input("Введите последовательность символов: ")

# Создание множества
char_set = set()

# Добавление букв от 'A' до 'F' и от 'X' до 'Z' в множество
for char in sequence:
    if char.isalpha():
        if char >= 'A' and char <= 'F' or char >= 'X' and char <= 'Z':
            char_set.add(char)

# Вывод множества букв от 'A' до 'F' и от 'X' до 'Z'
print("Множество букв от 'A' до 'F' и от 'X' до 'Z':", char_set)