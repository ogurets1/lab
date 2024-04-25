# Ввод строки
text = input("Введите строку: ")

# Находим индекс точки с запятой
semicolon_index = text.find(";")

# Подсчитываем количество символов до точки с запятой
characters_before_semicolon = semicolon_index

print("Количество символов до точки с запятой:", characters_before_semicolon)
