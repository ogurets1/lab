# Ввод строки
string = input("Введите строку, состоящую из нескольких слов, разделенных пробелами: ")

# Нахождение длины самого короткого слова
min_length = min(len(word) for word in string.split())

# Вывод результата
print("Длина самого короткого слова:", min_length)