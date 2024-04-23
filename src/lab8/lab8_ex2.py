# Ввод строки
sentence = input("Введите строку, заканчивающуюся точкой: ")

# Удаление точки в конце строки, если она есть
if sentence.endswith('.'):
    sentence = sentence[:-1]

# Разделение строки на слова
words = sentence.split()

# Подсчет количества слов
word_count = len(words)

# Вывод результата
print("Количество слов в строке:", word_count)