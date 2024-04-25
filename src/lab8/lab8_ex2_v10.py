# Ввод строки
text = input("Введите строку: ")

# Находим индекс точки с запятой
semicolon_index = text.find(";")

# Подсчитываем количество символов после точки с запятой
characters_after_semicolon = len(text) - semicolon_index - 1

print("Количество символов после точки с запятой:", characters_after_semicolon)
