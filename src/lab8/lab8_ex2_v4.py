# Ввод строки
text = input("Введите строку: ")

# Подсчет количества символов "*" и ";"
count_star = text.count('*')
count_semicolon = text.count(';')

print("Количество символов '*' в строке:", count_star)
print("Количество символов ';' в строке:", count_semicolon)
