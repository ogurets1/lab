# Ввод строки
string = input("Введите строку: ")

# Удаление пробелов
string = string.replace(" ", "")

# Удаление повторяющихся символов
unique_chars = "".join(set(string))

# Вывод результата
print("Результат:", unique_chars)
