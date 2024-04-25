# Ввод строки
string = input("Введите строку, состоящую из нескольких слов, разделенных пробелами: ")

# Преобразование строки
transformed_string = ":".join(sorted("".join(string.split())))

# Вывод результата
print("Результат:", transformed_string)