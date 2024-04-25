# Ввод имени файла
filename = input("Введите имя файла: ")

# Находим расширение файла
file_extension = filename.split(".")[-1]

# Вывод расширения файла
print("Расширение файла:", file_extension)
