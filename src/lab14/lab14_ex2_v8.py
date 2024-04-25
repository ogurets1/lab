# Ввод данных
list1 = input("Введите элементы первого списка через пробел: ").split()
list2 = input("Введите элементы второго списка через пробел: ").split()

# Создание словаря
dictionary = {list1[i]: list2[i] for i in range(len(list1))}

# Вывод
print(dictionary)