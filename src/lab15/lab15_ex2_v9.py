def extract_and_append(numbers_string, numbers_list):
    extracted_numbers = list(map(int, numbers_string.split(';')))
    numbers_list.extend(extracted_numbers)

# Ввод строки с клавиатуры
numbers_string = input("Введите строку с целыми числами, разделенными точкой с запятой: ")

# Ввод списка с клавиатуры
numbers_list = list(map(int, input("Введите список целых чисел, разделенных пробелами: ").split()))

# Вызов функции
extract_and_append(numbers_string, numbers_list)
print("Обновленный список чисел:", numbers_list)