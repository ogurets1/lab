import module1

# Ввод списка чисел и порядкового номера элемента с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
index = int(input("Введите порядковый номер элемента для удаления: "))

# Вызов функции для удаления элемента
module1.remove_element_by_index(numbers, index)

# Вывод результата
print("Список после удаления элемента:", numbers)
