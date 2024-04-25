# Ввод строки
text = input("Введите текст на английском: ")

# Разбиваем строку на слова
words = text.split()

# Инициализируем счетчик слов, начинающихся с буквы "b"
b_words_count = 0

# Перебираем слова и увеличиваем счетчик, если слово начинается с буквы "b"
for word in words:
    if word.startswith('b') or word.startswith('B'):
        b_words_count += 1

print("Количество слов, начинающихся с буквы 'b':", b_words_count)
