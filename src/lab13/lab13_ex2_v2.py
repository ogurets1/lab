# Ввод строки
string = input("Введите строку: ")

# Подсчет максимального количества встречающихся букв
max_count = max(string.lower().count(char) for char in string.lower() if char.isalpha())

# Вывод результата
print("Максимальное количество встречающихся букв:", max_count)