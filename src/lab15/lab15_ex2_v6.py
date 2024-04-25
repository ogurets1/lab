def print_or_add(phrase, phrases):
    if phrase in phrases:
        print(phrase)
    else:
        phrases.append(phrase)

# Ввод списка с клавиатуры
phrases = input("Введите список фраз, разделенных пробелами: ").split()

# Ввод фразы для поиска
phrase_to_find = input("Введите фразу для поиска: ")

# Вызов функции
print_or_add(phrase_to_find, phrases)
print("Обновленный список фраз:", phrases)