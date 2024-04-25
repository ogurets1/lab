def count_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    print("Количество букв верхнего регистра:", upper_count)
    print("Количество букв нижнего регистра:", lower_count)

# Ввод строки с клавиатуры
string = input("Введите строку: ")

# Вызов функции
count_letters(string)