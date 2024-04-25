import module1

# Ввод списка чисел, значений K и M с клавиатуры
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
k = int(input("Введите значение K: "))
m = int(input("Введите значение M: "))

# Вызов функции для замены значений элементов
module1.replace_values(numbers, k, m)

# Вывод результата
print("Список после замены значений:", numbers)