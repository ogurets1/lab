# Ввод слова
word = input("Введите слово: ")

# Проверка, является ли слово идентификатором
if word[0].isalpha() or word[0] == "_":
    if all(char.isalnum() or char == "_" for char in word):
        print("Слово является идентификатором")
    else:
        print("Слово не является идентификатором")
else:
    print("Слово не является идентификатором")
