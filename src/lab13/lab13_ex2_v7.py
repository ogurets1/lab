# Ввод строки
string = input("Введите строку, состоящую из нескольких слов, разделенных пробелами: ")

# Преобразование строки
transformed_string = "+".join(word[::-1] for word in string.split()[::-1])

# Вывод результата
print("Результат:", transformed_string)