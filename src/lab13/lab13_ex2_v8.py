# Ввод строки
string = input("Введите строку, состоящую из нескольких слов, разделенных пробелами: ")

# Нахождение длины самого длинного слова
max_length = max(len(word) for word in string.split())

# Вывод результата
print("Длина самого длинного слова:", max_length)