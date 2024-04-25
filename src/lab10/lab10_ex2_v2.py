# Ввод строки
sequence = input("Введите последовательность символов: ")

# Создание множества
char_set = set()

# Добавление букв от 'A' до 'Z' и цифр от '0' до '5' в множество
for char in sequence:
    if char.isalpha():
        if char >= 'A' and char <= 'Z' or char >= '0' and char <= '5':
            char_set.add(char)

# Вывод множества букв и цифр
print("Множество букв и цифр:", char_set)