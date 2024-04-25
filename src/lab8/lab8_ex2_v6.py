# Ввод строки
text = input("Введите строку: ")

# Удаление символов "_"
text_without_underscore = text.replace("_", "")

# Подсчет длины строки без символов "_"
length_without_underscore = len(text_without_underscore)

print("Текст без символов '_', длина:", length_without_underscore)
print("Текст без символов '_':", text_without_underscore)
